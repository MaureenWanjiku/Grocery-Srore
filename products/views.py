from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from .models import Product, Cart
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    # cart_count = request.session.get('cart-count', 0)
    return render(request, 'index.html', {'products': products})


def new(request):
    return render(request, 'new.html')

def product_details(request, id):
    products = Product.objects.get(id=id)
    return render(request, 'product_details.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    print(f'Requested product ID: {product_id}')
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.add_product(product)
    # request.session['cart_count'] = cart.total_items()
    return JsonResponse({'success': True, 'cart_count': cart.total_items()})