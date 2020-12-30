from django.db import models




class Formation(models.Model):
	name=models.CharField(max_length=1000)
	description=models.TextField()

	def __str__(self):
		return self.name


class University(models.Model):
	name=models.CharField(max_length=1000)
	description=models.TextField()
	formation=models.ManyToManyField(Formation,null=True,blank=True)
	image=models.ImageField()
	url=models.TextField(max_length=1000)


	def __str__(self):
		return self.name
