from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('signup/', views.register, name='signup'),
    path('login/', views.login_view, name='login'),  # Use your custom login view
    path('logout/', views.logout_view, name='logout'),
    path('supplier-dashboard/', views.supplier_dashboard, name='supplier_dashboard'),
    path('vendor-dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
]
