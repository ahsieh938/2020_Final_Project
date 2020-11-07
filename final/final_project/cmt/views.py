from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from invoice.models import Order
from django.utils import timezone


class ContractListView(LoginRequiredMixin, ListView):
    template_name = 'cmt/home.html'
    context_object_name = 'orders'
    queryset = Order.objects.filter(product__in=[9001]).order_by('-contract_end')
    paginate_by = 10

def search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, 'cmt/search.html')

