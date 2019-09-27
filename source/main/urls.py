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

from webapp.views import IndexView, MissionView, MissionCreateView, mission_delete_view, mission_update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('mission/<int:pk>/', MissionView.as_view(), name='mission_view'),
    path('mission/add/', MissionCreateView.as_view(), name='mission_add'),
    path('mission/<int:pk>/update/', mission_update_view, name='mission_update'),
    path('mission/<int:pk>/delete/', mission_delete_view, name='mission_delete'),
]
