from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WifiInfo(models.Model):
	router_name = models.CharField(max_length=128)
	password = models.CharField(max_length=128)
class Location(models.Model):
	location = models.CharField(max_length=128)
class Shuttle(models.Model):
	time = models.DateField()
	capacity = models.IntegerField()
	num_signedup = models.IntegerField()
	num_checkedin = models.IntegerField()
	num_on_waitlist = models.IntegerField()
	departure_location = models.ForeignKey(Location, related_name='departure_location')
	arrival_location = models.ForeignKey(Location, related_name='arrival_location')
class Racker(models.Model):
	user = models.OneToOneField(User)
	username = models.CharField(max_length=128)
	name = models.CharField(max_length=128)
	phone = models.CharField(max_length=64)
	checked_in_morning = models.ForeignKey(Shuttle, null=True, related_name='checked_in_morning')
	waiting_for_morning = models.ForeignKey(Shuttle, null=True, related_name='waiting_for_morning')
	signed_in_morning = models.ForeignKey(Shuttle, null=True, related_name='signed_in_morning')
	signed_in_afternoon = models.ForeignKey(Shuttle, null=True, related_name='signed_in_afternoon')
	checked_in_afternoon = models.ForeignKey(Shuttle, null=True, related_name='checked_in_afternoon')
	waiting_for_afternoon = models.ForeignKey(Shuttle, null=True, related_name='waiting_for_afternoon')

