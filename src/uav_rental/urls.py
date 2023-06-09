"""uav_rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler403, handler404, handler500
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.views.static import serve

schema_view = get_schema_view(
   openapi.Info(
      title="Uav Rental",
      default_version='v1',
      description="Uav Rental Project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('admin/', admin.site.urls),
    path('api/v1/', include("uav_rental.api_routes")),
    path('', include('apps.uav.urls')),
    path('account/', include('apps.account.urls')),
    path('order/', include('apps.order.urls')),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]


handler404 = 'apps.uav.views.custom_page_not_found_view'
handler500 = 'apps.uav.views.custom_error_view'
handler403 = 'apps.uav.views.custom_permission_denied_view'
handler400 = 'apps.uav.views.custom_bad_request_view'

