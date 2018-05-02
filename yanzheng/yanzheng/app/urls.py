from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^code/$',views.get_code),
	url(r'^userlogin/$',views.user_login),
]


