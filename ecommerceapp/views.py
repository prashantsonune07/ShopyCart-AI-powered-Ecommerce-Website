from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from ecommerceapp.models import Contact, Product, OrderUpdate, Orders
from django.contrib import messages
from math import ceil
import json
import random

# Create your views here.

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    selected_category = (request.GET.get('category') or 'all').strip()

    if selected_category.lower() == 'all':
        # Pick random 5 products from different categories.
        categories = list(
            Product.objects.values_list('category', flat=True).distinct()
        )
        random.shuffle(categories)

        selected_products = []
        for category in categories[:5]:
            product = Product.objects.filter(category=category).order_by('?').first()
            if product:
                selected_products.append(product)

        # Fallback: if unique categories are fewer than 5, fill remaining slots randomly.
        if len(selected_products) < 5:
            selected_ids = [p.id for p in selected_products]
            needed = 5 - len(selected_products)
            filler_products = Product.objects.exclude(id__in=selected_ids).order_by('?')[:needed]
            selected_products.extend(list(filler_products))
    else:
        # Pick random 5 products only from the requested category.
        selected_products = list(
            Product.objects.filter(category__iexact=selected_category).order_by('?')[:5]
        )

    content = {'allProds': allProds,
               'products': selected_products,
               'selected_category': selected_category,

               }

    if request.GET.get('partial') == '1':
        html = render_to_string('partials/product_cards.html', content, request=request)
        return JsonResponse({
            'html': html,
            'selected_category': selected_category,
        })

    return render(request, "index.html", content)


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/auth/login')

    if request.method == "POST":
        items_json  = request.POST.get('itemsJson', '')
        name        = request.POST.get('name', '')
        amount      = request.POST.get('amt', 0)
        email       = request.POST.get('email', '')
        address1    = request.POST.get('address1', '')
        address2    = request.POST.get('address2', '')
        city        = request.POST.get('city', '')
        state       = request.POST.get('state', '')
        zip_code    = request.POST.get('zip_code', '')
        phone       = request.POST.get('phone', '')

        # Save order to database
        Order = Orders(
            items_json=items_json,
            name=name,
            amount=amount,
            email=email,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            phone=phone,
            paymentstatus="PAID",
            amountpaid=str(amount),
        )
        Order.save()

        # Save order update
        update = OrderUpdate(
            order_id=Order.order_id,
            update_desc="Order placed successfully. Payment received."
        )
        update.save()

        # Return success — payment page shows confetti
        return render(request, 'checkout.html', {'thank': True, 'id': Order.order_id})

    return render(request, 'checkout.html')


def payment(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/auth/login')
    return render(request, 'payment.html')


def groupdeals(request):
    return render(request, 'groupdeals.html')


def allproducts(request):
    selected_category = (request.GET.get('category') or 'all').strip()

    products = Product.objects.all().order_by('category', 'product_name')
    if selected_category.lower() != 'all':
        products = products.filter(category__iexact=selected_category)

    categories = ['all'] + list(
        Product.objects.values_list('category', flat=True).distinct().order_by('category')
    )
    paginator = Paginator(products, 20)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'products': page_obj.object_list,
        'page_obj': page_obj,
        'total_products': products.count(),
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'allproducts.html', context)


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/auth/login')

    currentuser = request.user.username
    items = Orders.objects.filter(email=currentuser)
    rid = ""

    for i in items:
        myid = i.oid
        if myid:
            rid = myid.replace("ShopyCart", "")

    status = []
    if rid:
        try:
            status = OrderUpdate.objects.filter(order_id=int(rid))
        except:
            status = []

    context = {"items": items, "status": status}
    return render(request, "profile.html", context)


# ← ADDED: Ping endpoint for UptimeRobot keep-alive
def ping(request):
    return HttpResponse("OK")
