
from django.urls import path
from . import views

urlpatterns = [
    # Route for your Bootstrap homepage
    path('', views.home, name='home'),
    
    # Dynamic route for viewing a seller profile (e.g., /seller/5/)
    path('seller/<int:seller_id>/', views.seller_detail, name='seller_detail'),
]