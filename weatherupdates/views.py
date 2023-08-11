
import requests

from datetime import datetime

from django.shortcuts import render, redirect
import json

from django.contrib.auth import logout
from django.contrib import messages

def index(request):
    return render(request, 'weatherupdates/home.html')
    

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("weather:home")