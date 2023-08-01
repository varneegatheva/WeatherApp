from django.urls import path
from . import views

app_name = "accounts"   


urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("", views.login_request, name="login"),
    path("add_city", views.add_city_to_favourites, name='add_city')
]