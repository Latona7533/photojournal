
from django.urls import path, include
from accounts.views import ProfileView, UserRegistration

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>', ProfileView.as_view()),
    path('register/', UserRegistration.as_view()),
]