"""GreenData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
#from . import views
from .views import HomeView, ProductDetailView, AddProductView, UpdateProductView, DeleteProductView, AboutUsView

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings


urlpatterns = [
    #path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('product/<int:pk>', ProductDetailView.as_view(), name="productDetail"),
    path('addProduct/', AddProductView.as_view(), name="addProduct"),
    path('product/edit/<int:pk>', UpdateProductView.as_view(), name="updateProduct"),
    path('product/<int:pk>/delete', DeleteProductView.as_view(), name="deleteProduct"),
    path('aboutus/', AboutUsView, name='aboutus'),
	#path('category/<str:cats>/', CategoryView, name='category'),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")))
]