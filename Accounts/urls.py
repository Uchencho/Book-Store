from django.urls import path, include
from .views import homepage, signup, login, home

urlpatterns = [
    path('', homepage, name='homepage'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
]
