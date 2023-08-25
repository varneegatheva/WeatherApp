
import django
import requests

from datetime import datetime

from django.shortcuts import render, redirect
import json

from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.decorators.cache import cache_control
@login_required
def index(request):
	if not request.user.is_authenticated:
		return redirect((""))
	else:
		return render(request, 'weatherupdates/home.html')
    

def logout_request(request):
    # if request.method == "POST":
	username = request.POST.get('username')
	password = request.POST.get('password')

	print("username", username)
	print("password", password)
	logout(request)
	del request.session['username':username]
	del request.session['password':password]
	del request.delete_cookie['username': username]
	del request.delete_cookie['password':password]
	username2 = request.POST.get('username')
	password2 = request.POST.get('password')
	print("username2", username)
	print("password2", password)
	return redirect("weather:home")
