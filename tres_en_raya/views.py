from django.shortcuts import render

def tres_en_raya(request):

    if request.method == 'POST':

        tablero = list(request.POST.get('tablero'))
        turno = request.POST.get('turno')
        posicion = int(request.POST.get('posicion'))

        if tablero[posicion] == '-':
            tablero[posicion] = turno

        if turno == 'X':
            turno = 'O'
        else:
            turno = 'X'

        mensaje = 'Turno de ' + turno
        terminado = False

    else:

        tablero = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        turno = 'X'
        mensaje = 'Turno de X'
        terminado = False

    contexto = {
        'tablero': tablero,
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
    }

    return render(request, 'tres_en_raya.html', contexto)