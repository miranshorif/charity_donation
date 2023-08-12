from django.shortcuts import render,redirect
from .models import Organization,Donation,Campaign
# Create your views here.
def home(request):
    organizations = Organization.objects.all()
    return render(request, 'acccounts/home.html', {'organizations': organizations})

def donate(request, org_id):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        org = Organization.objects.get(pk=org_id)
        user = request.user
        Donation.objects.create(user=user, organization=org, amount=amount)
        return redirect('donation_history')
    else:
        org = Organization.objects.get(pk=org_id)
        return render(request, 'acccounts/donate.html', {'org': org})

def donation_history(request):
    donations = Donation.objects.filter(user=request.user)
    return render(request, 'acccounts/donation_history.html', {'donations': donations})
