from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import CustomUser

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, max_length=150)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	

# class AddCityForm(forms.Form):
#     city_name = forms.CharField(max_length=100, label='City Name')