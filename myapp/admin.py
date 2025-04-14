from django.contrib import admin
from .models import Service, Portfolio, ContactMessage
# Register your models here.


admin.site.register(Service)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    search_fields = ('name', 'category')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    readonly_fields = ('name', 'email', 'message', 'sent_at')
