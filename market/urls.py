from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('signup/', views.signup, name='signup'),
    path('signup/buyer/', views.buyer_signup, name='buyer_signup'),
    path('signup/buyer/email/', views.email_signup, name='email_signup'),
    path('account/', views.my_account, name='my_account'),
    path('logout/', views.logout_view, name='logout'),
] 