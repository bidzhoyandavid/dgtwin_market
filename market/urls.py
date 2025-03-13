from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
] 