from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import FormActions
from .models import Invoice, Order

class InvoiceForm(forms.ModelForm):
    invoice_num = forms.CharField(label="Invoice Number")
    invoice_date = forms.DateField(
        label="Invoice Date",
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
    )
    ship_date = forms.DateField(
        label="Ship Date",
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
    )
    po_num = forms.CharField(
        label="PO Number",
        required=False
    )

    end_user = forms.CharField(
        label="End User",
        required=False
    )

    class Meta:
        model = Invoice
        fields = ['invoice_num', 'customer', 'po_num', 'invoice_date', 'ship_date', 'currency', 'carrier', 'end_user']


class OrderForm(forms.ModelForm):
    user_num = forms.CharField(label="User Number")
    contract_start = forms.DateField(
        label="Contract Start-Date",
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        required=False
    )
    contract_end = forms.DateField(
        label="Contract End-Date",
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        required=False
    )

    serial = forms.CharField(
        label="DBMaker Serial ID",
        required=False
    )

    class Meta:
        model = Order
        fields = '__all__'


# class SearchForm(forms.ModelForm):
#     customer = forms.CharField()
#     startdate = forms.DateField(label="Contract Start-Date",
#         widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
#         required=False)
#     enddate = forms.DateField(label="Contract Start-Date",
#         widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
#         required=False)
#     class Meta:
#         model = Order
#         fields = '__all__'