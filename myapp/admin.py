from django.contrib import admin
from . models import Seller
from .models import ContactMessage

admin.site.register(Seller)
# Register your models here.

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')