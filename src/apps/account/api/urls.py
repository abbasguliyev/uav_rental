from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from apps.account.api.views import UserViewSet, LoginView

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename="user")

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path('', include(router.urls)),
]
