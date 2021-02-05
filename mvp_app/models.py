from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	full_name = models.CharField(max_length=60)
	image = models.ImageField(upload_to="static/user_pic")
	city = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published', auto_now_add=True)

	def __str__(self):
		return self.full_name

class Project(models.Model):
	title = models.CharField(max_length=60)
	image = models.ImageField(upload_to="static/project_image", null=True, blank=True)
	description = models.TextField()
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	profile = models.ForeignKey(
		Profile, 
		on_delete=models.CASCADE,
		related_name='project'
		)


	def __str__(self):
		return self.title
