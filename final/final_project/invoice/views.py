from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Sum
from .forms import OrderForm, InvoiceForm
from .models import Invoice, Customer, Currency, Order, Carrier
from django.template.defaulttags import register
from datetime import datetime
import simplejson as json


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = 'invoice/home.html'
    context_object_name = 'invoices'
    ordering = ['-pk']
    paginate_by = 10


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    exclude = ['creator']

    def get_form_class(self):
        return InvoiceForm
        
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class InvoiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Invoice
    exclude = ['creator']

    def get_form_class(self):
        return InvoiceForm
        
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class InvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Invoice
    success_url = '/invoice/list/'
    

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = '__all__'
    

    def get_form_class(self):
        return OrderForm

    def get_success_url(self, **kwargs):
        #return self.request.GET.get('next')
        return '/invoice/'+self.request.POST.get('invoice')

    def form_valid(self, form):
        return super().form_valid(form)


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    
    def get_success_url(self, **kwargs):
        return self.request.GET.get('next')
    

def order_create_view(request, invoice_num):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    form = OrderForm(request.POST or None) 
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/invoice/'+invoice_num)
    
    form.fields['invoice'].initial = invoice_num
    
    context = {
        'form': form,
        'invoice_num': invoice_num
    }

    return render(request, 'invoice/order_form.html', context)


def detail(request, invoice_num):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    try:
        invoice = Invoice.objects.get(pk=invoice_num)
    except Invoice.DoesNotExist:
        raise Http404("Invoice does not exist")
    context = {
        "invoice": invoice,
        "customers": Customer.objects.all(),
        "currencies": Currency.objects.all(),
        "orders": Order.objects.filter(invoice=invoice_num),
        "amount": Order.objects.filter(invoice=invoice_num).aggregate(Sum('amount')),
        "carriers": Carrier.objects.all(),
    }

    return render(request, 'invoice/detail.html', context)


def search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        if request.method == "POST":
            customer = request.POST["customer"]
            startstring = request.POST["start"]
            endstring = request.POST["end"]
            preliminary = Invoice.objects.all()
            if (len(startstring) == 0 and len(endstring) != 0) or (len(startstring) != 0 and len(endstring) == 0):
                return render(request, 'invoice/search.html', {"results": []})
            if ((len(customer) == 0 and len(startstring) == 0) and len(endstring) == 0):
                return render(request, 'invoice/search.html', {"results": []})
            if len(customer) != 0:
                preliminary = preliminary.filter(customer = Customer.objects.get(name__contains = customer))
            if len(startstring) != 0:
                startdate = datetime(int(startstring[6:10]), int(startstring[0:2]), int(startstring[3:5]))
                enddate = datetime(int(endstring[6:10]), int(endstring[0:2]), int(endstring[3:5]))
                if enddate >= startdate:
                    preliminary = preliminary.filter(invoice_date__lte = enddate)
                    preliminary = preliminary.filter(invoice_date__gte = startdate)
                else:
                    return render(request, 'invoice/search.html', {"results": []})
            return render(request, 'invoice/search.html', {"results": preliminary.order_by('-pk')})
        else:
            return render(request, 'invoice/search.html', {"results": []})

# def results(request, customer, startstring, endstring):
#     preliminary = Invoice.objects.all()
#     if (len(startstring) == 0 and len(endstring) != 0) or (len(startstring) != 0 and len(endstring) == 0):
#         print(1)
#         return []
#     if ((len(customer) == 0 and len(startstring) == 0) and len(endstring) == 0):
#         print(2)
#         return []
#     if len(customer) != 0:
#         print(3)
#         preliminary = preliminary.filter(customer = Customer.objects.get(name = customer))
#     if len(startstring) != 0:
#         startdate = datetime(int(startstring[6:10]), int(startstring[0:2]), int(startstring[3:5]))
#         enddate = datetime(int(endstring[6:10]), int(endstring[0:2]), int(endstring[3:5]))
#         if enddate >= startdate:
#             print(4)
#             preliminary = preliminary.filter(invoice_date__lte = enddate)
#             preliminary = preliminary.filter(invoice_date__gte = startdate)
#         else:
#             print(5)
#             return []]
#     return preliminary.order_by('-pk')


@register.filter
def get_range(value):
    return range(1, value + 1)

# def valid_range(startdate, enddate):
#     if year1 > year2:
#         return False
#     elif year1 == year2:
#         if month1 > month2:
#             return False
#         elif month1 == month2:
#             if day1 > day2:
#                 return False
#     return True

# def valid_date(year, month, day):
#     longmonths = [1, 3, 5, 7, 8, 10, 12]
#     shortmonths = [4, 6, 9, 11]
#     if len(year) == 0 or int(year) > 2020 or year < 0:
#         return False
#     else:
#         if month == 2:
#             leap_year = is_leap_year(int(year))
#             if leap_year:
#                 limit = 29
#             else:
#                 limit = 28
#         else:
#             if month in longmonths:
#                 limit = 31
#             else:
#                 limit = 30
#     if day > limit:
#         return False
#     else:
#         return True
            


# def is_leap_year(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 == 0 and year % 400 != 0:
#         return False
#     else:
#         return True
    
    