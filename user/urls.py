import django


from django.urls import path
from .views import ShowProfilePageView, CreateProfilePageView


urlpatterns = [ 
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
  
  ]