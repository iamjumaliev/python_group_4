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

from webapp.views import IndexView, MissionView, MissionCreateView, mission_delete_view, mission_update_view, \
    StatusView, StatusCreateView, status_update_view, status_delete_view, TypeView, TypeCreateView, type_update_view, \
    type_delete_view, Status_View, Type_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('mission/<int:pk>/', MissionView.as_view(), name='mission_view'),
    path('mission/add/', MissionCreateView.as_view(), name='mission_add'),
    path('mission/<int:pk>/update/', mission_update_view, name='mission_update'),
    path('mission/<int:pk>/delete/', mission_delete_view, name='mission_delete'),
    path('status/', StatusView.as_view(), name='status'),
    path('status/<int:pk>/', Status_View.as_view(), name='status_view'),
    path('status/add/',  StatusCreateView.as_view(), name='status_add'),
    path('status/<int:pk>/update/',  status_update_view, name='status_update'),
    path('status/<int:pk>/delete/',status_delete_view, name='status_delete'),
    path('type/', TypeView.as_view(), name='type'),
    path('type/<int:pk>/', Type_View.as_view(), name='type_view'),
    path('type/add/', TypeCreateView.as_view(), name='type_add'),
    path('type/<int:pk>/update/', type_update_view, name='type_update'),
    path('type/<int:pk>/delete/', type_delete_view, name='type_delete'),

]
