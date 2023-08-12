from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, DonationType, DonarAddress,Donar
from .constants import GENDER_CHOICES

class RegistrationForm(UserCreationForm):
    account_type = forms.ModelChoiceField(queryset=DonationType.objects.all())
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    street_address = forms.CharField(max_length=180)
    city = forms.CharField(max_length=180)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=180)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            account_type = self.cleaned_data['account_type']
            gender = self.cleaned_data['gender']
            date_of_birth = self.cleaned_data['date_of_birth']
            street_address = self.cleaned_data['street_address']
            city = self.cleaned_data['city']
            postal_code = self.cleaned_data['postal_code']
            country = self.cleaned_data['country']

            Donar.objects.create(
                user=user,
                account_type=account_type,
                gender=gender,
                date_of_birth=date_of_birth,
                account_no=(user.id + 1000000)
            )

            DonarAddress.objects.create(
                user=user,
                street_address=street_address,
                city=city,
                postal_code=postal_code,
                country=country
            )

        return user
