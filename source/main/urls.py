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

from webapp.views import IndexView, MissionView, MissionCreateView, MissionDeleteView, MissionUpdateView, \
    StatusCreateView, TypeView, TypeCreateView, TypeUpdateView, \
    TypeDeleteView, TypeIndexView,  StatusIndexView, StatusView,StatusUpdateView,StatusDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('mission/<int:pk>/', MissionView.as_view(), name='mission_view'),
    path('add/', MissionCreateView.as_view(), name='add'),
    path('mission/<int:pk>/update/', MissionUpdateView.as_view(), name='mission_update'),
    path('mission/<int:pk>/delete/', MissionDeleteView.as_view(), name='mission_delete'),
    path('status/', StatusIndexView.as_view(), name='status'),
    path('status/<int:pk>/', StatusView.as_view(), name='status_view'),
    path('status/add/',  StatusCreateView.as_view(), name='status_add'),
    path('status/<int:pk>/update/',  StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/delete/',StatusDeleteView.as_view(), name='status_delete'),
    path('type/', TypeIndexView.as_view(), name='type'),
    path('type/<int:pk>/', TypeView.as_view(), name='type_view'),
    path('type/add/', TypeCreateView.as_view(), name='type_add'),
    path('type/<int:pk>/update/', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete')

]
