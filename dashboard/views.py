from django.http import HttpResponse
from django.shortcuts import render

#Index Page
def index(request):
    return render(request, 'dashboard/index.html')

#Staff Deatils Page
def staff(request):
    return render(request, 'dashboard/staff.html')

#Product Deatils Page
def product(request):
    return render(request, 'dashboard/product.html')

#Order Deatils Page
def order(request):
    return render(request, 'dashboard/order.html')