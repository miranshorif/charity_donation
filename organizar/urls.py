from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donate, name='donate'),
    path('history/', views.donation_history, name='history')
]
