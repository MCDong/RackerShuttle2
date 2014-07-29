from django.shortcuts import render
from django.http import HttpResponse
from shuttle.models import *
from forms import *
from datetime import date, datetime, timedelta


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = RackerForm(request.POST)
        if form.is_valid():
            form.save()
    form = RackerForm()
    return render(request, 'index.html', {'form' : form})

def schedule(request):
    now = datetime.now()
    shuttles = Shuttle.objects.filter(time__gte=now)
    return render(request, 'schedule.html', {'shuttles' : shuttles})
