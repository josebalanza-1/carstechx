

from django.shortcuts import render


def tres_en_raya(request):

    # Retrieve the game information from the session
    tablero = request.session.get('tablero', ['-','-','-','-','-','-','-','-','-'])
    turno = request.session.get('turno', 'X')
    terminado = request.session.get('terminado', False)

    # Check all possible winning combinations
    combinaciones = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # Reset the game
    if request.method == 'POST' and 'reiniciar' in request.POST:
        request.session.flush()
        return render(request, 'tres_en_raya.html', {
            'tablero': ['-','-','-','-','-','-','-','-','-'],
            'turno': 'X',
            'mensaje': 'Turno de X',
            'terminado': False,
        })

    if request.method == 'POST' and not terminado:

        # Get the selected position from the form
        posicion = int(request.POST.get("posicion"))

        if tablero[posicion] == '-':
            tablero[posicion] = turno

            # Check if a player has won
            for combinacion in combinaciones:
                a, b, c = combinacion

                if tablero[a] == tablero[b] == tablero[c] and tablero[a] != '-':
                    terminado = True
                    mensaje = '¡Ha ganado ' + turno + '!'
                    break
            else:
                mensaje = ''

            # Check if the board is full
            if not terminado and '-' not in tablero:
                terminado = True
                mensaje = '¡Empate!'

            # Change the current turn
            if not terminado:
                if turno == 'X':
                    turno = 'O'
                else:
                    turno = 'X'

        if not terminado:
            mensaje = 'Turno de ' + turno

        # Save the updated game information in the session
        request.session['tablero'] = tablero
        request.session['turno'] = turno
        request.session['terminado'] = terminado

    else:
        mensaje = 'Turno de ' + turno

    # Prepare the context for the template
    contexto = {
        'tablero': tablero,
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
    }

    return render(request, 'tres_en_raya.html', contexto)

# from django.shortcuts import render


# def tres_en_raya(request):

#     # Retrieve the game information from the session
#     tablero = request.session.get('tablero', ['-','-','-','-','-','-','-','-','-'])
#     turno = request.session.get('turno', 'X')
#     terminado = request.session.get('terminado', False)

#     if request.method == 'POST' and not terminado:

#         # Get the selected position from the form
#         posicion = int(request.POST.get("posicion"))

#         if tablero[posicion] == '-':
#             tablero[posicion] = turno

#             # Check if the board is full
#             if '-' not in tablero:
#                 terminado = True

#             # Change the current turn
#             if turno == 'X':
#                 turno = 'O'
#             else:
#                 turno = 'X'

#         mensaje = 'Turno de ' + turno

#         # Save the updated game information in the session
#         request.session['tablero'] = tablero
#         request.session['turno'] = turno
#         request.session['terminado'] = terminado

#     else:
#         mensaje = 'Turno de ' + turno

#     # Prepare the context for the template
#     contexto = {
#         'tablero': tablero,
#         'turno': turno,
#         'mensaje': mensaje,
#         'terminado': terminado,
#     }

#     return render(request, 'tres_en_raya.html', contexto)