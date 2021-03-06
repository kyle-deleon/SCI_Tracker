"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index), #GET
    path('users', views.create_users), #POST
    path('login', views.login), #POST
    path('dashboard', views.dashboard), #GET
    # path('sports_cards', views.sports_cards),
    path('sports_cards/new', views.new_card), #GET
    path('sports_cards/create', views.create_card), #POST
    path('sports_cards/<int:id>', views.show_one),
    # path('sportds_cards/<int:id>/delete', views.delete_card),
    path('sports_cards/<int:id>/review', views.create_review), # POST
    # path('sports_cards/<int:id>/like', views.like),
    # path('sports_cards/<int:id>/unlike', views.unlike),
    # path('users/<int:id>', views.show_user),
    path('logout', views.logout)
]
