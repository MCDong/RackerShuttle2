from django.shortcuts import render
from django.http import HttpResponse
from forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = RackerForm(request.POST)
        if form.is_valid():
            form.save()
    form = RackerForm()
    return render(request, 'index.html', {'form' : form})
