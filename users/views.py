from django.shortcuts import render, redirect
from .models import User, edit_profile_form
from django.contrib import auth
from django.contrib.auth.decorators import login_required

    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username exists! Please try another username')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('Email exists! Please try another email')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, address=address, password=password1)
                user.save()
                return redirect('login')
        else:
            print('Passwords did not match!')
            return redirect('register')
    else:
        return render(request, 'users/register.html')
    

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request,user)
            print('Login Successfull!')
            return redirect('display_products')
        else:
            print('invalid credentials')
            return redirect('login') 
    else:
        return render(request, 'users/login.html')   


@login_required
def logout(request):
    auth.logout(request)
    print('User is logged out')
    return redirect('display_products')


@login_required
def view_profile(request):
    user = request.user  
    context = {'user': user}
    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = edit_profile_form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = edit_profile_form(instance=user)

    context = {'form': form}
    return render(request, 'users/edit_profile.html', context)