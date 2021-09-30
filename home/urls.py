from django.contrib import admin
from django.urls import path, include

from .views import *
app_name = 'home'
urlpatterns = [
    path('', handleLogin, name='login'),
    path('home', login_required(HomeView.as_view()), name='homes'),
    path('about/', login_required(HomeView.as_view(template_name='home/about_us.html')), name='about'),
    path('logout/', logoutuser, name='logout'),
    path('search/', search, name='search'),
    path('create/', product_create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('add/<int:pk>/', addqty, name='add'),
    path('edit/<int:pk>/',login_required(EditProdView.as_view()), name='edit'),
    path('supedit/<int:pk>/',login_required(EditSupplierView.as_view()), name='supedit'),
    path('createsupplier/',login_required(CreateSupplierView.as_view()), name='create-supplier'),
    path('contact/',login_required(CreateContactView.as_view()), name='contact'),
    path('products/', login_required(ProductListView.as_view()), name='product-list'),
    path('company/', login_required(CompanyListView.as_view()), name='company-list'),
    path('suppliers/', login_required(SupplierListView.as_view()), name='supplier-list'),
    path('sales/', login_required(SalesListView.as_view()), name='sales-list'),
    path('makebill/', makebill, name='makebill'),
    # path('create/', ProductCreate.as_view(), name='create'),


]
