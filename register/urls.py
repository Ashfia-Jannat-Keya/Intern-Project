from django.urls import path
from register import views

urlpatterns = [
	
	path("", views.index, name="index"),
	path("register/", views.register, name="register"),
	path("login/", views.login, name="login"),
	path("info/", views.info, name="info"),
	path("registerinfo/", views.registerinfo, name="registerinfo"),
	]