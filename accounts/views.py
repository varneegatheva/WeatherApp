from django.http import HttpResponse, JsonResponse
from django.shortcuts import  render, redirect

from accounts.models import FavouriteCity
from .forms import AddCityForm, NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("weather:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				print('REDIRECT IS GOING TO ')
				return redirect("weatherupdates:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form})

def add_city_to_favourites(request):
    city = request.POST['hiddenCity']
    # print('TYPE', type(city))
    # form2 = AddCityForm(request.POST)
    # print("request.post", request.POST)
    # print("BOOLEAN", form2.is_valid)
    # print("form2", form2)
    # print("clean_data", form2.cleaned_data)
    # city_name2 = form2.cleaned_data['city_name']
    # print("CITYNAME: ", city_name2)
    # if request.method == 'POST':
    #     form = AddCityForm(request.POST)
    #     if form.is_valid():
    #         city_name = form.cleaned_data['city_name']
    #         user = request.user  # Get the currently logged-in user
    #         favorite_city = FavouriteCity(user=user, city_name=city_name)
    #         favorite_city.save()
    #         if request.is_ajax():
    #             return JsonResponse({'status': 'success'}) # Return JSON response for AJAX request
    #         else:
    #             return redirect('favorites_list')  # Redirect to the list of favorite cities

    # else:
    #     form = AddCityForm()
	
	
	# return render(request, 'accounts/hi.html')
    return render(request, 'accounts/hi.html')

    # return render(request, 'add_city.html', {'form': form})
	# print("REQUEST': ", request)
	# print(request.POST)


