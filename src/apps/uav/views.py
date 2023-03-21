from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from apps.uav.selectors import uav_list, category_list, brand_list
from apps.uav.models import Uav, Category, Brand
from apps.uav.filters import UavFilter
from apps.uav.forms import UavForm, CategoryForm, BrandForm
from uav_rental.utils import generate_random_slug


class UavListView(ListView):
    model = Uav
    paginate_by = 4
    template_name = "home.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        filtered_queryset = UavFilter(self.request.GET, queryset=queryset).qs
        return filtered_queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = UavFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = filter
        queryset = filter.qs

        # Paginate the results
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['categories'] = category_list()
        context['brands'] = brand_list()
        context['filter'] = UavFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
class UavDetailView(DetailView):
    model = Uav
    template_name = "uav_detail.html"
    context_object_name = "uav"

class DashboardView(TemplateView):
    template_name = "uavs.html"

class UavDashboardListView(ListView):
    model = Uav
    paginate_by = 10
    template_name = "uavs.html"
    context_object_name = "uavs"

class UavAddView(LoginRequiredMixin, CreateView):
    form_class = UavForm
    success_url = reverse_lazy('uav_dashboard')
    template_name = 'uav_create.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})
    
    def form_valid(self, form):
        uav = form.save(commit=False)
        name = form.cleaned_data.get("name")
        slug = generate_random_slug(name=name, query_list=uav_list())
        uav.slug = slug
        uav.save()
        return super().form_valid(form)
    
class UavUpdateView(LoginRequiredMixin, UpdateView):
    model = Uav
    form_class = UavForm
    success_url = reverse_lazy('uav_dashboard')
    template_name = 'uav_update.html'
    context_object_name = "uav"

    def form_valid(self, form):
        uav = form.save(commit=False)
        name = form.cleaned_data.get("name")
        slug = generate_random_slug(name=name, query_list=uav_list())
        uav.slug = slug
        uav.save()
        return super().form_valid(form)

class UavDeleteView(LoginRequiredMixin, DeleteView):
    model = Uav
    success_url = reverse_lazy('uav_dashboard')
    template_name = 'uav_delete.html'
    context_object_name = "uav"

    def form_valid(self, form):
        messages.success(self.request, "The uav was deleted successfully.")
        return super(UavDeleteView,self).form_valid(form)
    
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    paginate_by = 10
    template_name = "category.html"
    context_object_name="categories"

class CategoryAddView(LoginRequiredMixin, CreateView):
    form_class = CategoryForm
    success_url = reverse_lazy('category')
    template_name = 'category_create.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})
    
    def form_valid(self, form):
        category = form.save(commit=False)
        name = form.cleaned_data.get("category_name")
        slug = generate_random_slug(name=name, query_list=category_list())
        category.slug = slug
        category.save()
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category')
    template_name = 'category_update.html'
    context_object_name = "category"

    def form_valid(self, form):
        category = form.save(commit=False)
        name = form.cleaned_data.get("category_name")
        slug = generate_random_slug(name=name, query_list=category_list())
        category.slug = slug
        category.save()
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category')
    template_name = 'category_delete.html'
    context_object_name = "category"

    def form_valid(self, form):
        messages.success(self.request, "The Category was deleted successfully.")
        return super(CategoryDeleteView,self).form_valid(form)
    

class BrandListView(LoginRequiredMixin, ListView):
    model = Brand
    paginate_by = 10
    template_name = "brand.html"
    context_object_name="brands"

class BrandAddView(LoginRequiredMixin, CreateView):
    form_class = BrandForm
    success_url = reverse_lazy('brand')
    template_name = 'brand_create.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})
    
    def form_valid(self, form):
        brand = form.save(commit=False)
        name = form.cleaned_data.get("brand_name")
        slug = generate_random_slug(name=name, query_list=brand_list())
        brand.slug = slug
        brand.save()
        return super().form_valid(form)


class BrandUpdateView(LoginRequiredMixin, UpdateView):
    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('brand')
    template_name = 'brand_update.html'
    context_object_name = "brand"

    def form_valid(self, form):
        brand = form.save(commit=False)
        name = form.cleaned_data.get("brand_name")
        slug = generate_random_slug(name=name, query_list=brand_list())
        brand.slug = slug
        brand.save()
        return super().form_valid(form)


class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = Brand
    success_url = reverse_lazy('brand')
    template_name = 'brand_delete.html'
    context_object_name = "brand"

    def form_valid(self, form):
        messages.success(self.request, "The Brand was deleted successfully.")
        return super(BrandDeleteView,self).form_valid(form)
    

def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})