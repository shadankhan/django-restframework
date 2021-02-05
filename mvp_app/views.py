from django.shortcuts import render
from mvp_app.models import Project, Profile
from mvp_app.serializers import ProjectSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

class Profile_list(generics.ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	
class Profile_detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class ProjectPagination(PageNumberPagination):
	page_size = 3

class Project_list(generics.ListCreateAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	pagination_class = ProjectPagination
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['title']


class Project_detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer


# ViewSets

# class Project_list(viewsets.ModelViewSet):
# 	queryset = Project.objects.all()
# 	serializer_class = ProjectSerializer



# Generics==========================================
# class Project_list(generics.ListCreateAPIView):
# 	queryset = Project.objects.all()
# 	serializer_class= ProjectSerializer

# class Project_detail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Project.objects.all()
# 	serializer_class = ProjectSerializer



# Mixin==============================================

# class Project_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
# 	queryset = Project.objects.all()
# 	serializer_class = ProjectSerializer

# 	def get(self, request):
# 		return self.list(request)

# 	def post(self, request):
# 		return self.create(request)

# class Project_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
# 	queryset =  Project.objects.all()
# 	serializer_class = ProjectSerializer

# 	def get(self, request, pk):
# 		return self.retrieve(request, pk)

# 	def put(self, request, pk):
# 		return self.update(request, pk)

# 	def delete(self, request, pk):
# 		return self.destroy(request, pk)



# class Based view==============================
# class Project_list(APIView):
# 	def get(self, request):
# 		project = Project.objects.all()
# 		serializer = ProjectSerializer(project, many=True)
# 		return Response(serializer.data)

# 	def post(self, request):
# 		serializer = ProjectSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Project_detail(APIView):
# 	def get_object(self, pk):
# 		try:
# 			return Project.objects.get(pk=pk)
# 		except Project.DoesNotExist:
# 			raise Http404

# 	def get(self, request,pk):
# 		project = self.get_object(pk)
# 		serializer = ProjectSerializer(project)
# 		return Response(serializer.data)

# 	def put(self, request, pk):
# 		project = self.get_object(pk)
# 		serializer = ProjectSerializer(project, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk):
# 		project = self.get_object(pk)
# 		project.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)



# Function Based View ======================

# Create your views here.
# @api_view(['GET'])
# def api(request):
# 	api_urls ={
# 	'project list and create': 'mvp/api/project_list',
# 	'project detail, update, delete':'mvp/api/project_dpd'
# 	}
# 	return Response(api_urls)

# @api_view(['GET', 'POST'])
# def project_list(request):
# 	if request.method == 'GET':		
# 		project = Project.objects.all()
# 		serializer = ProjectSerializer(project, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		serializer = ProjectSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def create_project(request):
# 	serializer = ProjectSerializer(data=request.data)
# 	if serializer.is_valid():
# 		serializer.save()
# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'PUT', 'DELETE'])
# def project_dpd(request, pk):
# 	try:	
# 		project = Project.objects.get(pk=pk)
# 	except Project.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method=='GET':
# 		serializer=ProjectSerializer(project)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer = ProjectSerializer(project, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors)

# 	elif request.method == "DELETE":
# 		project.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
