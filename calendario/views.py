from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import EventForm
from .models import Event
from django.http import HttpResponseRedirect

def calendario(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Fernando"
    month = month.capitalize()
    # convertir mes de str a int
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)


    # defino calendario
    cal = HTMLCalendar().formatmonth(year, month_number)

    # llamo al año actual
    now = datetime.now()
    current_year = now.year

    # la hora actual
    time = now.strftime('%H:%M')



    return render(request,
        'calendario/calendario.html',{
        "name" : name,
        "year" : year,
        "month" : month,
        "month_number" : month_number,
        "cal" : cal,
        "current_year" : current_year,
        "time" : time,
        })


def agregar_evento(request):
    submitted = False
    if request.method == 'POST':
        formulario = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agregar-evento?submitted=True')
    else:
        formulario = EventForm
        if 'submitted' in request.GET:
            submitted=True    

    formulario = EventForm
    return render(request, 'calendario/add_event.html', {'formulario':formulario, 'submitted':submitted})
