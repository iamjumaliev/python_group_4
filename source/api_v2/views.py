from django.shortcuts import render
from rest_framework import viewsets

from webapp.models import Project,Mission

from api_v2.serializers import ProjectSerializer, MissionSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer



# Create your views here.
