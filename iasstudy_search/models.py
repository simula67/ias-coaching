from django.db import models

# Create your models here.

class Field(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
                return self.name

class Position(models.Model):
	name = models.CharField(max_length=30)
	field = models.ForeignKey(Field)
	def __unicode__(self):
                return self.name
class Quote(models.Model):
	text = models.CharField(max_length=500)
	position = models.ForeignKey(Position)
	def __unicode__(self):
                return self.text
class Personality(models.Model):
	name = models.CharField(max_length=30)
	quotations = models.ManyToManyField(Quote)
	def __unicode__(self):
        	return self.name
	class Meta(object):
		verbose_name_plural = "Personalities"
