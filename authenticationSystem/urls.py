from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.accountsHomePage, name="accountsHomePage" ),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.loginUser, name='loginUser'),
]
