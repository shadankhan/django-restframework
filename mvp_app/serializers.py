from rest_framework import serializers
from mvp_app.models import Project, Profile

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields= '__all__'

class ProfileSerializer(serializers.ModelSerializer):
	project = ProjectSerializer(read_only=True, many=True)
	class Meta:
		model = Profile
		fields = '__all__'