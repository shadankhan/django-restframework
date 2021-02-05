from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mvp_app import views

# router = DefaultRouter()
# router.register('api/project', views.Project_list)

urlpatterns = [
	# path('', include(router.urls)),
	# path('api/', views.api, name='api'),
    path('api/project/', views.Project_list.as_view(), name='project_list'),
    # path('api/create_project', views.create_project, name='create_project'),
    path('api/project/<int:pk>', views.Project_detail.as_view(), name='project_dpd'),
    path('api/profile_list/', views.Profile_list.as_view(), name='profile_list'),
    path('api/profile/<int:pk>', views.Profile_detail.as_view(), name='profile_detail'),
]
