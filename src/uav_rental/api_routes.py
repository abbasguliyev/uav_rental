from django.urls import include, path

urlpatterns = [
    path("account/", include("apps.account.api.urls")),
    path("order/", include("apps.order.api.urls")),
    path("uav/", include("apps.uav.api.urls")),
]