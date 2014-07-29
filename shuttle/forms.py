from django import forms
from models import *
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.util import ErrorList
class RackerForm(forms.ModelForm):
	class Meta:
		model = Racker
		exclude = ['user','checked_in_morning', 'checked_in_afternoon', 'waiting_for_morning', 'waiting_for_afternoon', 'signed_in_morning', 'signed_in_afternoon', 'waitlist_signup_time_morning', 'waitlist_signup_time_afternoon']

class ShuttleForm(forms.ModelForm):
	class Meta:
		model = Shuttle
		exclude = ['num_signedup', 'num_checkedin']
