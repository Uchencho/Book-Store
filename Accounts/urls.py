from django.urls import path, include
from .views import homepage, signup

urlpatterns = [
    path('', homepage, name='homepage'),
    path('signup/', signup, name='signup'),
]
