from django.shortcuts import render, redirect

def homepage(request):
    return render(request, 'home.html')

def contacto(request):

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')

        contexto = {
            'nombre': nombre,
            'email': email,
            'telefono': telefono,
            'mensaje': mensaje
        }

        return render(request, 'contacto_recibido.html', contexto)

    return redirect('homepage')