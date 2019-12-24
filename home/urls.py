from django.urls import path, include
from .views import home, mylogout


urlpatterns = [
    path('', home, name="home"),
    path('logout/', mylogout, name="logout")
]