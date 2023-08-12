from django.contrib import admin
from .models import Organization, Campaign, Donation,Cause
# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display =['cause', 'goal_amount', 'deadline']
    list_filter = ['deadline',]
    
class DonationAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'donated_to']
    search_fields = ['user', 'amount', 'donated_to']
    
    
admin.site.register(Organization),
admin.site.register(Cause)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Donation, DonationAdmin)