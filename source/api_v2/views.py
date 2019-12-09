from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from webapp.models import Project,Mission
from rest_framework.permissions import SAFE_METHODS

from api_v2.serializers import ProjectSerializer, MissionSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()



class MissionViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()

# Create your views here.
