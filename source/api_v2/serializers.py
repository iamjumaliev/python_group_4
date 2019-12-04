from webapp.models import Project,Mission

from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class MissionSerializer(serializers.ModelSerializer):

    project = ProjectSerializer(many=True,read_only=True)

    class Meta:
        model = Mission
        fields = ('id', 'summary', 'description', 'status', 'type',
                  'project','created_at', 'updated_at', 'created_by', 'assigned_to')


