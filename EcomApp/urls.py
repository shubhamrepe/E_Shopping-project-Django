"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<int:pid>/', views.details, name='detail'),
    path('detail/cart/', views.cart, name='cart'),
    path('add_cart/<int:pid>/', views.add_cart, name='add_cart'),
    path('remove/<int:pid>/',views.remove, name='remove'),
    path('search/', views.search, name='search'),
    path('range/',views.range,name="range"),
    path('watchList/',views.watchList,name="watchList"),
    path('sort/',views.sort,name="sort"),
    path('hightolow/',views.hightolow,name="hightolow"),
    path('updateQty/<int:uval>/<int:pid>/',views.updateQty,name="updateQty"),
    path('register',views.register_user,name="register"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('viewOrder/',views.viewOrder,name="viewOrder"),
    path('payment/',views. makePayment,name="payment"),
    path('insertProd/',views.insertProduct,name="insertProd"),
]
