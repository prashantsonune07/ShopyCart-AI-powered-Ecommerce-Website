from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('all-products/', views.allproducts, name="allproducts"),
    path('profile/',views.profile,name="profile"),
    path('checkout/', views.checkout, name="Checkout"),
    path('payment/', views.payment, name="payment"),
    path('groupdeals/', views.groupdeals, name="groupdeals"),
    path('ping/', views.ping, name="ping"),  # ← ADDED for UptimeRobot keep-alive
]
