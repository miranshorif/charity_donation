from django.contrib import admin
from .models import User,Donar,DonarAddress,DonationType
# Register your models here.
class DonaterAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_type', 'account_no', 'gender', 'date_of_birth']
    list_filter  = ['account_type',]
admin.site.register(DonationType)
admin.site.register(User)
admin.site.register(DonarAddress)
admin.site.register(Donar)