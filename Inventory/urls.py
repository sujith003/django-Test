from django.urls import path
from .views import *

urlpatterns=[
    path('home/', homepage),
    path('about/', Aboutpage),
    path('contact/', Contactpage),
    path('services/', Servicespage),
    path('products/add/', productspage),
    path('allproducts/', AllProduct),
    path('products/delete/<int:id>', DeleteProduct, name='product_delete'),
    path('products/update/<int:id>', UpdateProduct, name='product_update'),
    path('products/add/', AddProduct, name='product_add'),
]