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
from django.urls import path, include

urlpatterns = [
    path('', include('apps.sports_cards.urls')),
    path('register'),
    path('login'),
    path('sports_cards'),
    path('sports_cards/new'),
    path('sports_cards/create'),
    path('sports_cards/<ind:id>'),
    path('sportds_cards/<int:id>/delete'),
    path('sports_cards/<int:id>/review'),
    path('sports_cards/<int:id>/like'),
    path('sports_cards/<int:id>/unlike'),
    path('users/<int:id>'),
    path('logout')
]
