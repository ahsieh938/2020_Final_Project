from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    address1 = models.CharField(max_length=200, null=True, blank=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.company}"


class Carrier(models.Model):
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class ContractType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    
class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Invoice(models.Model):
    invoice_num = models.CharField(max_length=10, primary_key=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.PROTECT)
    invoice_date = models.DateField()
    ship_date = models.DateField()
    po_num = models.CharField(max_length=10, null=True, blank=True)
    currency = models.ForeignKey(Currency, null=True, on_delete=models.SET_NULL)
    carrier = models.ForeignKey(Carrier, null=True, on_delete=models.SET_NULL)
    end_user = models.CharField(max_length=100, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.invoice_num

    def get_absolute_url(self):
        return reverse('inv-detail', kwargs={'invoice_num': self.invoice_num})

    
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=0)

    def __str__(self):
        return f"{self.id} - {self.name}"

    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    amount = models.DecimalField(decimal_places=2, max_digits=7)
    user_num = models.IntegerField(null=True, blank=True)
    contract_type = models.ForeignKey(ContractType, null=True, blank=True, on_delete=models.SET_NULL)
    contract_start = models.DateField(null= True, blank=True)
    contract_end = models.DateField(null=True, blank=True)
    serial = models.CharField(max_length=10, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"{self.product} - {self.invoice} - {self.quantity} - {self.amount}"


