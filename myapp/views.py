
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Seller
from .models import ContactMessage

def home(request):
    """Processes search bar text and redirects to the correct profile."""
    # Look for the 'q' parameter in the URL query string (e.g., /?q=3)
    search_id = request.GET.get('q', '').strip()
    
    if search_id:
        try:
            # Look up the seller using the auto-generated database ID
            seller = Seller.objects.get(id=search_id)
            # Redirect to the 'seller_detail' URL pattern name, passing the ID
            return redirect('seller_detail', seller_id=seller.id)
        except (ValueError, Seller.DoesNotExist):
            # If the ID isn't found or isn't a valid number, generate a Bootstrap-friendly alert
            messages.error(request, f"No seller found with ID: {search_id}")
            
    # If no ID was searched, just render your home page template normally
    return render(request, 'home.html')

def seller_detail(request, seller_id):
    """Renders the profile page for a specific seller ID."""
    # Fetch the seller data or raise a 404 page if they don't exist
    seller = get_object_or_404(Seller, id=seller_id)
    return render(request, 'seller_detail.html', {'seller': seller})
# Create your views here.


def contact_view(request):
    if request.method == "POST":
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to database
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'home.html')