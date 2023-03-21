from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.contrib.auth import get_user_model
from apps.account.forms import RegisterForm, LoginForm, UpdateUserForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Sign Up View
class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class()
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return render(request, self.template_name, context={'form': form})
        

class LoginView(View):
    form_class = LoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get(self, request):
        form = self.form_class()
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return render(request, self.template_name, context={'form': form})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse_lazy('home'))
                else:
                    messages.error(request, 'Disabled Account')
            else:
                messages.error(request, 'Check Your Username and Password')

        return render(request, self.template_name, context={'form': form})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))

class ProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UpdateUserForm
    success_url = reverse_lazy('home')
    template_name = 'profile.html'
    context_object_name = "user"

    