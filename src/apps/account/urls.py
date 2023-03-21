from django.urls import path
from apps.account import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("<int:pk>/", views.ProfileView.as_view(), name="profile"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
