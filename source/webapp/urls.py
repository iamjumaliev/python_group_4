from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, MissionView, MissionCreateView, MissionDeleteView, MissionUpdateView, \
    StatusCreateView, TypeView, TypeCreateView, TypeUpdateView, \
    TypeDeleteView, TypeIndexView, StatusIndexView, StatusView, StatusUpdateView, StatusDeleteView, ProjectIndexView, \
    ProjectView, ProjectDeleteView, ProjectCreateView,ProjectUpdateView

app_name = 'webapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('mission/<int:pk>/', MissionView.as_view(), name='mission_view'),
    path('add/project/<int:pk>/mission/', MissionCreateView.as_view(), name='add'),
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
    path('type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),
    path('project/', ProjectIndexView.as_view(), name='project'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/add/',ProjectCreateView.as_view(),name='project_add'),
    path('project/<int:pk>/update',ProjectUpdateView.as_view(),name='project_update')
]