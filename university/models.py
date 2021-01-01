from django.db import models




class Formation(models.Model):
	name=models.CharField(max_length=1000)
	description=models.TextField()

	def __str__(self):
		return self.name


class Universitie(models.Model):
	name=models.CharField(max_length=1000)
	description=models.TextField()
	#formation=models.ManyToManyField(Formation,null=True,blank=True)
	#image=models.ImageField()
	image=models.TextField()
	url=models.TextField(max_length=1000)
	localisation=models.TextField(max_length=1000)
	prix=models.IntegerField()


	def __str__(self):
		return self.name
