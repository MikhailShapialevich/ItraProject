from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, CreateShirtForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Shirt

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user, 
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'acctivate_acc.html')
    
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, 'acctivated_done.html')
    else:
        return HttpResponse('Activation link is invalid!')

def personal(request):
    if request.user.is_authenticated:
       return render(request, 'registration/personal.html')
    else:
        return redirect('http://localhost:8000/user/login')


def home(request):
    return render(request, 'home.html')

def shirt(request):
    return render(request, 'shirt.html')

def create_shirt(request):
    form = CreateShirtForm()
    return render(request, 'create_shirt.html', {'form': form})

def shirt_list(request):
    shirts = Shirt.objects.all()
    return render(request, 'OurProject/Shirt/list.html', {'shirts': shirts})

def shirt_detail(request, pk):
    shirt = get_object_or_404(Shirt, pk=pk)
    return render(request,'OurProject/Shirt/detail.html', {'shirt': shirt})