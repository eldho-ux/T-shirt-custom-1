"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myprojectapp.views import home
from myprojectapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cart/',views.cart, name='cart'),
    path('custom/', views.custom_tshirt, name='custom_tshirt'),
    path('create/', views.create_tshirt, name='create_tshirt'),
    path('tshirt_success/',views.tshirt_success, name='tshirt_success'),
    path('remove-from-cart/<int:tshirt_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('edit-cart-item/<int:tshirt_id>/', views.edit_cart_item, name='edit_cart_item'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)