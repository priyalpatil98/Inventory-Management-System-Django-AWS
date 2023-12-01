from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Index Page
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = orders.count() # To get Orders count to display on Admin Dashboard
    products_count = products.count() # To get  products count to display on Admin Dashboard
    workers_count = User.objects.all().count() # To get Staff's count to display on Admin Dashboard
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            Order.send_confirmation_email(instance.staff)
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders' : orders,
        'form' : form,
        'products' : products,
        'orders_count' : orders_count,
        'workers_count' : workers_count,
        'products_count' : products_count,
    }
    return render(request, 'dashboard/index.html', context)

#Staff Deatils Page
@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count() # To get Staff's count to display on Admin Dashboard
    orders_count = Order.objects.all().count() # To get Orders count to display on Admin Dashboard
    products_count = Product.objects.all().count() # To get  products count to display on Admin Dashboard
    context = {
        'workers' : workers,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'products_count' : products_count,
    }
    return render(request, 'dashboard/staff.html', context)

#Product Deatils Page
@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all() #ORM 'SELECT * FROM dashboard_product'
    products_count = items.count() # To get  products count to display on Admin Dashboard
    workers_count = User.objects.all().count() # To get Staff's count to display on Admin Dashboard
    orders_count = Order.objects.all().count() # To get Orders count to display on Admin Dashboard

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added successfully!') #Flash Message
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    context ={
        'items' : items,
        'form' : form,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'products_count' : products_count,
    }
    return render(request, 'dashboard/product.html', context)

#Deleting Product Page
@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.warning(request, f'Item has been deleted successfully!') #Flash Message
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

#Editing Product Page
@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Item has been Edited successfully!') #Flash Message
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form' : form,
    }
    return render(request, 'dashboard/product_update.html', context)

#Order Deatils Page
@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    orders_count = Order.objects.count() # To get Orders count to display on Admin Dashboard
    workers_count = User.objects.all().count() # To get Staff's count to display on Admin Dashboard
    products_count = Product.objects.all().count() # To get  products count to display on Admin Dashboard
    context = {
        'orders' : orders,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'products_count' : products_count,
    }
    return render(request, 'dashboard/order.html', context)

#Staff Details Page
@login_required(login_url='user-login')
def staff_detail(request, pk):
    worker = User.objects.get(id=pk)
    workers = User.objects.all()
    workers_count = workers.count() # To get Staff's count to display on Admin Dashboard
    orders_count = Order.objects.all().count() # To get Orders count to display on Admin Dashboard
    products_count = Product.objects.all().count() # To get  products count to display on Admin Dashboard
    context = {
        'worker' : worker,
        'workers' : workers,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'products_count' : products_count,
    }
    return render(request, 'dashboard/staff_detail.html', context)

#def profile(request):
 #   return render(request, 'dashboard/profile.html')