
# Create your views here.
from django.shortcuts import render
from datetime import datetime

def calendario(request, fecha):

    mi_fecha = datetime.strptime(fecha, '%Y-%m-%d')
    mi_dia = mi_fecha.day
    mi_mes = mi_fecha.month
    mi_ano = mi_fecha.year
    mensaje = "Bienvenido al calendario"

    return render(request, 'calendario/fecha.html', {
        'dia': mi_dia,
        'mes': mi_mes,
        'ano': mi_ano,
        'mensaje': mensaje
    })