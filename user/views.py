from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.db import transaction, IntegrityError

def register(request):
    if request.method == 'POST':
        try:
            # Get user_type directly from the radio button
            user_type = request.POST.get('user_type')
            
            # Enhanced debugging
            print("=" * 50)
            print("REGISTRATION DEBUG INFO:")
            print(f"Raw POST data: {dict(request.POST)}")
            print(f"user_type received: '{user_type}'")
            print(f"All form field names: {list(request.POST.keys())}")
            print("=" * 50)
            
            # Extract other form data
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
                messages.error(request, "Username already exists. Please choose a different username.")
                return render(request, 'user/signup.html')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered. Please use a different email.")
                return render(request, 'user/signup.html')

            # Validate user_type
            valid_types = ['supplier', 'vendor']
            if user_type not in valid_types:
                print(f"ERROR: Invalid user_type '{user_type}', forcing to vendor")
                user_type = 'vendor'

            print(f"FINAL user_type being saved: '{user_type}'")

            # Use database transaction to ensure data consistency
            with transaction.atomic():
                # Create User
                user = User.objects.create_user(
                    username=username,
                    email=email,  
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )

                # Create UserProfile
                user_profile, created = UserProfile.objects.get_or_create(
                    user=user,
                    defaults={
                        'user_type': user_type,
                        'phone': phone or '',
                        'company_name': company_name or '',
                        'location': location
                    }
                )
                
                print(f"UserProfile created with user_type: '{user_profile.user_type}'")

            # Login the user after successful registration
            auth_login(request, user)  
            
            # Display proper success message based on user type
            if user_type == 'supplier':
                messages.success(request, f"Welcome {first_name}! Your supplier account has been created successfully.")
                return redirect('supplier_dashboard')
            else:
                messages.success(request, f"Welcome {first_name}! Your vendor account has been created successfully.")
                return redirect('vendor_dashboard')
                
        except Exception as e:
            print(f"Registration error: {str(e)}")
            messages.error(request, "Registration failed due to an unexpected error. Please try again.")
            return render(request, 'user/signup.html')

    return render(request, 'user/signup.html')


def login_view(request):
    if request.method == 'POST':
        email_or_username = request.POST.get('email_or_username', '').strip()
        password = request.POST.get('password', '').strip()
        
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
                pass
        
        if user is not None:
            auth_login(request, user)
            
            try:
                profile = user.userprofile
                
                # Automatic redirection based on user type
                if profile.user_type == 'supplier':
                    messages.success(request, f'Welcome back, {user.first_name or user.username}! Redirecting to Supplier Dashboard.')
                    return redirect('supplier_dashboard')
                elif profile.user_type == 'vendor':
                    messages.success(request, f'Welcome back, {user.first_name or user.username}! Redirecting to Vendor Dashboard.')
                    return redirect('vendor_dashboard')
                else:
                    messages.warning(request, f'User type not recognized. Please contact support.')
                    return redirect('index')
                        
            except UserProfile.DoesNotExist:
                messages.error(request, 'User profile not found. Please contact support.')
                return redirect('login')
        else:
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
    if not hasattr(request.user, 'userprofile'):
        messages.error(request, 'User profile not found.')
        return redirect('login')
    
    if request.user.userprofile.user_type != 'supplier':
        messages.error(request, 'Access denied. Supplier access only.')
        return redirect('vendor_dashboard' if request.user.userprofile.user_type == 'vendor' else 'login')
    
    context = {
        'username': request.user.username,
        'user': request.user,
        'user_profile': request.user.userprofile,
    }
    
    return render(request, 'user/supplier_dashboard.html', context)

@login_required
def vendor_dashboard(request):
    if not hasattr(request.user, 'userprofile'):
        messages.error(request, 'User profile not found.')
        return redirect('login')
    
    if request.user.userprofile.user_type != 'vendor':
        messages.error(request, 'Access denied. Vendor access only.')
        return redirect('supplier_dashboard' if request.user.userprofile.user_type == 'supplier' else 'login')
    
    context = {
        'username': request.user.username,
        'user': request.user,
        'user_profile': request.user.userprofile,
    }
    
    return render(request, 'user/vendor_dashboard.html', context)