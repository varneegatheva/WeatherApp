from django.urls import path 
from . import views # imports all the Views from the weatherupdates/views.py file

app_name = "weatherupdates"

urlpatterns = [
    # the actual path, the view, and the view's name
    path('', views.index, name='home'), # name here is specific to URL pattern
    path("logout/", views.logout_request, name= "logout")
]
