from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import TokenGenerator, generate_token
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_str as force_text
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if password != confirm_password:
            messages.warning(request, "Password is Not Matching")
            return render(request, 'signup.html')

        try:
            if User.objects.get(username=email):
                messages.info(request, "Email is Taken")
                return render(request, 'signup.html')
        except Exception as identifier:
            pass

        user = User.objects.create_user(email, email, password)
        user.is_active = False
        user.save()

        # ── Use the real deployed domain, not localhost ──
        domain = request.get_host()
        protocol = 'https' if request.is_secure() else 'http'

        email_subject = "Activate Your ShopyCart Account"
        message = render_to_string('activate.html', {
            'user': user,
            'domain': domain,
            'protocol': protocol,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user),
        })

        try:
            email_message = EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            email_message.send()
            messages.success(
                request,
                "✅ Account created! Please check your email and click the activation link."
            )
        except Exception as e:
            # If email fails, show the activation link directly on screen as fallback
            activation_link = f"{protocol}://{domain}/auth/activate/{urlsafe_base64_encode(force_bytes(user.pk))}/{generate_token.make_token(user)}/"
            messages.warning(
                request,
                f"Account created but email could not be sent. "
                f"Please click this link to activate your account: {activation_link}"
            )

        return redirect('/auth/login/')

    return render(request, "signup.html")


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "✅ Account Activated Successfully! You can now sign in.")
            return redirect('/auth/login')

        return render(request, 'activatefail.html')


def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']
        myuser = authenticate(username=username, password=userpassword)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/auth/login')

    return render(request, 'login.html')


def handlelogout(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect('/auth/login')


class RequestResetEmailView(View):
    def get(self, request):
        return render(request, 'request-reset-email.html')

    def post(self, request):
        email = request.POST['email']
        user = User.objects.filter(email=email)

        if user.exists():
            # ── Use the real deployed domain, not localhost ──
            domain = request.get_host()
            protocol = 'https' if request.is_secure() else 'http'

            email_subject = '[ShopyCart] Reset Your Password'
            message = render_to_string('reset-user-password.html', {
                'domain': domain,
                'protocol': protocol,
                'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token': PasswordResetTokenGenerator().make_token(user[0]),
            })

            try:
                email_message = EmailMessage(
                    email_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                email_message.send()
                messages.info(
                    request,
                    "✅ Password reset link has been sent to your email."
                )
            except Exception as e:
                reset_link = f"{protocol}://{domain}/auth/reset-password/{urlsafe_base64_encode(force_bytes(user[0].pk))}/{PasswordResetTokenGenerator().make_token(user[0])}/"
                messages.warning(
                    request,
                    f"Could not send email. Please use this link to reset your password: {reset_link}"
                )

        else:
            messages.warning(request, "No account found with that email address.")

        return render(request, 'request-reset-email.html')


class SetNewPasswordView(View):
    def get(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token,
        }
        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.warning(request, "Password Reset Link is Invalid or Expired")
                return render(request, 'request-reset-email.html')

        except DjangoUnicodeDecodeError as identifier:
            pass

        return render(request, 'set-new-password.html', context)

    def post(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token,
        }
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if password != confirm_password:
            messages.warning(request, "Passwords are Not Matching")
            return render(request, 'set-new-password.html', context)

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            messages.success(request, "✅ Password Reset Successful! Please login with your new password.")
            return redirect('/auth/login/')

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request, "Something Went Wrong. Please try again.")
            return render(request, 'set-new-password.html', context)
