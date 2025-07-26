from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def register(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        terms = request.POST.get('terms')

        # Validation
        if not all([first_name, last_name, username, email, password, confirm_password, location]):
            messages.error(request, "All required fields must be filled.")
            return render(request, 'user/signup.html')

        if not terms:
            messages.error(request, "You must agree to the terms and conditions.")
            return render(request, 'user/signup.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'user/signup.html')

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return render(request, 'user/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'user/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'user/signup.html')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,  
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            UserProfile.objects.create(
                user=user,
                user_type=user_type,
                email=email,
                phone=phone,
                company_name=company_name,
                location=location
            )

            auth_login(request, user)  
            messages.success(request, "Account created successfully!")
            
            print(f"DEBUG: User {user.username} registered with type: {user_type}")
            
            # Redirect based on user type after registration
            if user_type == 'supplier':
                return redirect('supplier_dashboard')
            elif user_type == 'regular':
                return redirect('vendor_dashboard')
            else:
                return redirect('index')
                
        except Exception as e:
            messages.error(request, f"An error occurred during registration: {str(e)}")
            return render(request, 'user/signup.html')

    return render(request, 'user/signup.html')


def login_view(request):
    if request.method == 'POST':
        email_or_username = request.POST.get('email_or_username', '').strip()
        password = request.POST.get('password', '').strip()
        
        # Validation for empty fields
        if not email_or_username or not password:
            messages.error(request, 'Please enter both email/username and password.')
            return render(request, 'user/login.html')
        
        # Try to authenticate with username first
        user = authenticate(request, username=email_or_username, password=password)
        
        # If that fails, try to find user by email and authenticate with username
        if user is None:
            try:
                user_obj = User.objects.get(email=email_or_username)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                print(f"DEBUG: No user found with email: {email_or_username}")
                pass
        
        if user is not None:
            auth_login(request, user)
            try:
                profile = user.userprofile
                print(f"DEBUG: User {user.username} logged in with user_type: {profile.user_type}")
                
                if profile.user_type == 'supplier':
                    return redirect('supplier_dashboard')
                elif profile.user_type == 'regular':
                    return redirect('vendor_dashboard')
                else:
                    messages.error(request, f'Unknown user type: {profile.user_type}')
                    return redirect('index')
            except UserProfile.DoesNotExist:
                messages.error(request, 'User profile not found.')
                return redirect('login')
        else:
            print(f"DEBUG: Authentication failed for: {email_or_username}")
            messages.error(request, 'Invalid email/username or password.')
    
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')  


def homepage(request):
    return render(request, 'user/index.html')


# Dashboard views
@login_required
def supplier_dashboard(request):
    print(f"DEBUG: Accessing supplier dashboard - User: {request.user.username}")
    
    if not hasattr(request.user, 'userprofile'):
        messages.error(request, 'User profile not found.')
        return redirect('login')
    
    print(f"DEBUG: User type: {request.user.userprofile.user_type}")
    
    if request.user.userprofile.user_type != 'supplier':
        messages.error(request, 'Access denied. Supplier access only.')
        return redirect('login')
    
    # Pass username and other context data
    context = {
        'username': request.user.username,
        'user': request.user,
    }
    
    return render(request, 'user/supplier_dashboard.html', context)



@login_required
def vendor_dashboard(request):
    print(f"DEBUG: Accessing vendor dashboard - User: {request.user.username}")
    
    if not hasattr(request.user, 'userprofile'):
        messages.error(request, 'User profile not found.')
        return redirect('login')
    
    print(f"DEBUG: User type: {request.user.userprofile.user_type}")
    
    if request.user.userprofile.user_type != 'regular':
        messages.error(request, 'Access denied. Vendor access only.')
        return redirect('login')
    
    return render(request, 'user/vendor_dashboard.html')
