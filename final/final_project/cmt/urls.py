from django.urls import path
from . import views
from .views import ContractListView

urlpatterns = [
    path('home/', ContractListView.as_view(), name='cmt-home')
]