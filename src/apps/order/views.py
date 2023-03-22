from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic import View

from django.urls import reverse_lazy
from apps.order.models import Order
from apps.order.forms import OrderForm


class OrderListView(LoginRequiredMixin, ListView):
    """
    This view is for the list all orders in dashboar.
    """
    model = Order
    paginate_by = 10
    template_name = "order.html"
    context_object_name="orders"

class OrderAddView(LoginRequiredMixin, View):
    """
    This view is for the add new order. 
    When user click the order button inside uav card in home page this view start working
    """
    form_class = OrderForm
    template_name = 'home.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order completed successfully")
            return redirect(reverse_lazy('home'))
        return render(request, self.template_name, context={'form': form})



class OrderDeleteView(LoginRequiredMixin, DeleteView):
    """
    This view is for the delete order.
    """
    model = Order
    success_url = reverse_lazy('order')
    template_name = 'order_delete.html'
    context_object_name = "order"

    def form_valid(self, form):
        messages.success(self.request, "The Order was deleted successfully.")
        return super(OrderDeleteView,self).form_valid(form)
    