from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about),
    path('store', views.store),
    path('products', views.products),
    path('dolls_collection', views.dolls_collection),
    path('product_template', views.product_template),
    path('dolls/caoilin', views.caoilin),
    path('dolls/tiffany', views.tiffany),
    path('dolls/jenny', views.jenny),
    path('dolls/daithi', views.daithi),
    path('animals/peaches', views.peaches),
    path('', views.index),
]
