from django.shortcuts import redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

class UserTypeRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only redirect authenticated users
        if request.user.is_authenticated:
            try:
                if hasattr(request.user, 'userprofile'):
                    current_path = request.path
                    user_type = request.user.userprofile.user_type
                    
                    # Define role-based access rules
                    try:
                        supplier_dashboard_path = reverse('supplier_dashboard')
                        vendor_dashboard_path = reverse('vendor_dashboard')
                        
                        # Redirect suppliers trying to access vendor areas
                        if user_type == 'supplier' and current_path == vendor_dashboard_path:
                            return redirect('supplier_dashboard')
                        
                        # Redirect vendors trying to access supplier areas  
                        if user_type == 'vendor' and current_path == supplier_dashboard_path:
                            return redirect('vendor_dashboard')
                    except:
                        # If URL patterns don't exist yet, skip redirection
                        pass
            except (ObjectDoesNotExist, AttributeError):
                # Handle cases where userprofile doesn't exist
                pass

        response = self.get_response(request)
        return response
