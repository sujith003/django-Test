from django.shortcuts import render, redirect
from .forms import *
from .models import *

def homepage(request):

    data={
        "name":"Sujith",
        "role":"Saketh",
        "numbers":[1,3,4,67],
        "marks":{
            "tamil":99,
            "english":93
        }
    }
    return render(request, 'home.html',data)

def Aboutpage(request):
    return render(request, 'about.html')

def Contactpage(request):
    return render(request, 'contact.html')

def Servicespage(request):
    return render(request, 'service.html')

def productspage(request):

    context={
        'product_form': product_Form()
    }

    if request.method == "POST":
        product_form=product_Form(request.POST)

        if product_form.is_valid():
            product_form.save()

    return render(request, 'products.html',context)

def AllProduct(request):
    
    context={
        "all_products" : Product.objects.all()
    }

    return render(request, 'show.html', context)

def DeleteProduct(request,id):
    selected_product=Product.objects.get(id=id)
    selected_product.delete()

    return redirect('/inventory/allproducts/')

def UpdateProduct(request,id):
    selected_product= Product.objects.get(id=id)
    context={
        "product_form" : product_Form(instance=selected_product)
    }

    if request.method=='POST':
        product_form=product_Form(request.POST,instance=selected_product)
        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/allproducts/')
            
    return render(request,'products.html',context)




def AddProduct(request):
    context={
        'product_form': product_Form()
    }

    if request.method == "POST":
        product_form=product_Form(request.POST)

        if product_form.is_valid():
            product_form.save()

    return render(request, 'products.html',context)