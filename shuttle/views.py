from django.shortcuts import render
from django.http import HttpResponse
from shuttle.models import *
from forms import *
from datetime import date, datetime, timedelta
from django.db.models import Q



# Create your views here.
def index(request):
    # If shuttles haven't been created for today, create them
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

def wait_list(request, sid):
    shuttle = Shuttle.objects.get(id=sid)
    q = Q(waiting_for_morning__id=sid) | Q(waiting_for_afternoon__id=sid)
    waitlist = Racker.objects.filter(q)
    if shuttle.time 
    return render(request, 'wait_list.html', {'waitlist' : waitlist})