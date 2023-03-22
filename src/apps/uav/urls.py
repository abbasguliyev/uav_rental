from django.urls import path
from apps.uav import views

urlpatterns = [
    path("", views.UavListView.as_view(), name="home"),
    path("dashboard/category/", views.CategoryListView.as_view(), name="category"),
    path("category-create/", views.CategoryAddView.as_view(), name="category_add"),
    path("category-update/<slug:slug>/", views.CategoryUpdateView.as_view(), name="category_update"),
    path("category-delete/<slug:slug>/", views.CategoryDeleteView.as_view(), name="category_delete"),
    path("dashboard/brand/", views.BrandListView.as_view(), name="brand"),
    path("brand-create/", views.BrandAddView.as_view(), name="brand_add"),
    path("brand-update/<slug:slug>/", views.BrandUpdateView.as_view(), name="brand_update"),
    path("brand-delete/<slug:slug>/", views.BrandDeleteView.as_view(), name="brand_delete"),
    path("uav-create/", views.UavAddView.as_view(), name="uav_add"),
    path("uav-update/<slug:slug>/", views.UavUpdateView.as_view(), name="uav_update"),
    path("uav-delete/<slug:slug>/", views.UavDeleteView.as_view(), name="uav_delete"),
    path("dashboard/uavs/", views.UavDashboardListView.as_view(), name="uav_dashboard"),
    path("<slug:slug>/", views.UavDetailView.as_view(), name="uav-detail"),
]
