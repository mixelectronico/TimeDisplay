from django.shortcuts import render
from datetime import datetime
import locale

# Create your views here.
def index(request):
    locale.setlocale(locale.LC_TIME, 'es_CL')
    date = datetime.now().strftime("%d de %B del %Y")
    time = datetime.now().strftime("%H:%M:%S %p")
    context = {'date': date, 'time': time}
    return render(request, 'index.html', context)