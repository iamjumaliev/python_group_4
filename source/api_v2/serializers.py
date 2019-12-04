from webapp.models import Project,Mission

from rest_framework import serializers



class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = ('id', 'summary', 'description', 'status', 'type',
                  'project','created_at', 'updated_at', 'created_by', 'assigned_to')


class ProjectSerializer(serializers.ModelSerializer):

    mission_project = MissionSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'updated_at','mission_project')