from django.urls import path
from .views import CreateUserView

urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    # Add other URL patterns as needed
]