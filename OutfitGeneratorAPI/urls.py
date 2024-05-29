"""
URL configuration for OutfitGeneratorAPI project.

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
from django.contrib import admin
from django.urls import path
from OutfitGeneratorAPI import views
from OutfitGeneratorAPI.views import UserCreate, UserDetail, UserAuthentication

urlpatterns = [
    path('', views.welcome),
    path('admin/', admin.site.urls),
    path('pieces/', views.piece_list, name='piece_list'),
    path('pieces/<uuid:id>', views.piece_detail),
    path('outfits/', views.outfit_list),
    path('piece_category', views.piece_category),
    path('outfits/create/', views.create_outfit),
    path('outfits/<uuid:outfit_id>/', views.update_outfit),
    path('usuario/', UserCreate.as_view(), name='user-create'),
    path('usuario/<str:username>/', UserDetail.as_view(), name='user-detail'),
    path('authenticate_or_create_user/', UserAuthentication.as_view(), name='authenticate_or_create_user')
]
