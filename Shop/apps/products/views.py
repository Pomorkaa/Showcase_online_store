from django.shortcuts import render
from django.http import HttpResponse
from.models import Product
# Create your views here.

app_name = 'products'
def index(request):
    return HttpResponse("Я работаю!")

def index(request):
    new_product = Product.objects.order_by('product_name')[:10]
    return render(request, 'products/list.html', {'product': new_product})

def detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Exception:
        return HttpResponse('SDSFSDFDSF SDFSDFSDFSDFSD FSDFSDF')
    return render(request, 'products/product.html', {'product': product})

def img(request):
    num_img = Product.objects.all().count()
    return render(request, 'products/list.html', context={'num_img': num_img})

