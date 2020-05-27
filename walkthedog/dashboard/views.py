from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from walkthedog.dashboard.forms import ClientOrderFrom
from walkthedog.dashboard.models import Order


# Create your views here.


class ClientOrderView(LoginRequiredMixin, CreateView):
    template_name = "dashboard/client_order.html"
    form_class = ClientOrderFrom

    def get_success_url(self):
        return reverse_lazy('dashboard:filter_orders')

    def get_form_kwargs(self):
        kwargs = super(ClientOrderView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        print(self.request.user)
        return kwargs


class FilterOrdersView(LoginRequiredMixin, ListView):
    template_name = "dashboard/filter_orders.html"
    def get_queryset(self):
        return Order.objects.all()

    def get_success_url(self):
        return reverse_lazy('dashboard:list_orders')

class FilterReviewOrderView(LoginRequiredMixin, ListView):
    template_name = "dashboard/review_order.html"
    def get_queryset(self):
        return Order.objects.all()

    def get_success_url(self):
        return reverse_lazy('dashboard:home')

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('author-list')
