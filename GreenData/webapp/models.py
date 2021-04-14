from djongo import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.



class PackagingInfo(models.Model):
	#_id = models.AutoField()
	element_name = models.CharField(max_length=255)
	material_name = models.CharField(max_length=255)
	mass = models.IntegerField()
	is_recycled = models.BooleanField()

	def __str__(self):
		return f'{element_name}: {material_name}'
	
	#class Meta:
		# I think this makes the object to not be registerable alone in the database
		#abstract = True


class Product(models.Model):
	#ObjectId = models.AutoField()
	product_name = models.CharField(max_length=255)
	packaging = models.CharField(max_length=255)
	#packaging = models.ArrayField(model_container=PackagingInfo)
	packaging_mass = models.IntegerField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.product_name

	def get_absolute_url(self):
		return reverse('productDetail', args=(str(self.id)) )
