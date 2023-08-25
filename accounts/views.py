from django.http import HttpResponse, JsonResponse
from django.shortcuts import  render, redirect

from accounts.models import FavouriteCity
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("weatherupdates:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/register.html", context={"register_form":form})

# @never_cache
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
				return redirect("weatherupdates:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form})

def add_city_to_favourites(request):
    user = request.user
    favourite_city_name = request.POST['hiddenCity']
    favourite_city = FavouriteCity(user=user, city_name=favourite_city_name)
    favourite_city.save()
    # message = f"You submitted the city: {favourite_city_name}"
    return render(request=request, template_name="weatherupdates/home.html") 

def get_favourites(request):
	queryset = FavouriteCity.objects.all()
	cities = [city.city_name for city in queryset]
	context = {'cities': cities}
	html_template = get_html_template(cities)
	return render(request=request, template_name="accounts/favourites.html", context=context)


def get_html_template(cities):

	template = """
	<div class="card">
		<div class="card-body">
			<div id="city-time" class="card-text float-end"></div>
			<img id="city-icon" src="http://openweathermap.org/img/w/{{ icon }}.png" alt="">
			<div id="city-description" class="card-text"><h6></h6></div>
			<div id="city-name" class="card-text"><h8></h5></div>
			<div id="city-countrycode" class="card-text"><h8></h5></div>
			<div id="city-temp" class="card-text"><h6></h6></div>
			<div id="city-wind" class="card-text"><h6></h6></div>
			<div id="city-humidity" class="card-text"><h6></h6></div>
		</div>
	</div>
	"""

	print(template)
	# for city in cities:
	# 	full_template = full_template + template
	# print(full_template)
	# return full_template
	pass





# def get_html_template(cities):
# 	full_template = """   
# 	<div class="card">
# 		<div class="card-body">
# 			<div id="city-time" class="card-text float-end"></div>
# 			<img id="city-icon" src="http://openweathermap.org/img/w/{{ icon }}.png" alt="">
# 			<div id='city-description' class="card-text"><h6></h6></div>
# 			<div id='city-name' class="card-text"><h8></h5></div>
# 			<div id='city-countrycode' class="card-text"><h8></h5></div>
# 			<div id="city-temp" class="card-text"><h6></h6></div>
# 			<div id='city-wind' class="card-text"><h6></h6></div>
# 			<div id='city-humidity' class="card-text"><h6></h6></div>
# 		</div>
# 	</div>
# 	"""

# 	template = """   
# 	<div class="card">
# 		<div class="card-body">
# 			<div id="city-time" class="card-text float-end"></div>
# 			<img id="city-icon" src="http://openweathermap.org/img/w/{{ icon }}.png" alt="">
# 			<div id='city-description' class="card-text"><h6></h6></div>
# 			<div id='city-name' class="card-text"><h8></h5></div>
# 			<div id='city-countrycode' class="card-text"><h8></h5></div>
# 			<div id="city-temp" class="card-text"><h6></h6></div>
# 			<div id='city-wind' class="card-text"><h6></h6></div>
# 			<div id='city-humidity' class="card-text"><h6></h6></div>
# 		</div>
# 	</div>
# 	"""
# 	for city in cities:
# 		full_template = full_template + template
# 	print(full_template)
# 	return full_template