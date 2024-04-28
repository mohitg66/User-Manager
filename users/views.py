from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import CustomUser, Skill
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        skills = request.POST.getlist('skills')

        # Create the user
        user = CustomUser.objects.create_user(username=username, password=password, gender=gender)
        user.save()
        
        for skill in skills:
            try:
                user.skills.add(Skill.objects.get(name=skill))
            except Skill.DoesNotExist:
                messages.error(request, f'Skill "{skill}" does not exist')
        user.save()

        login(request, user)
        messages.success(request, 'User registered successfully')
        return redirect('users:index')
    return render(request, 'users/index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(username, password)

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log in the user
            login(request, user)
            messages.success(request, 'User logged in successfully')
            return redirect('users:index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'User logged out successfully')
    return redirect('users:index')