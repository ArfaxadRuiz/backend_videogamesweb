from django.urls import path
from .views import UserListCreateView, UserDetailView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('', UserListCreateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    
]

