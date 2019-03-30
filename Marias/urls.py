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
    path('', views.index),
]
