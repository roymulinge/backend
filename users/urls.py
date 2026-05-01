from django.urls import path
from . import views
from .views import ProfileView

app_name = 'users'
urlpatterns = [
    path('phone-number/', views.phone_number_required_view, name='phone-number-required'),
    path('profile/', ProfileView.as_view(), name='user-profile'),
]