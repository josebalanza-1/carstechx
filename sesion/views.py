# from django.shortcuts import render

# # Create your views here.
# def ejemplo (request):
#     context = dict()
#     if request.session.get('nombres'):
#         context = {
#             nombre = request.session.get('nombres')
#         }
#     if request.method == 'POST' :
#         nombre = request.POST.get('nombre', '')
#         nombres = request.POST.get('nombres', '')
#         nombres += nombre + '\n'
#         request.session['nombres'] = nombres
#         context = {
#             'nombre' = nombres,
#         }
#     return render(request, 'ejemplo.html', context)

# def juego(request):
#     if request.session.get('palabra'):
#         palabra = request.session.get('palabra')
#         adivinado = request.session.get('adivinado')
#         if request.method == 'POST' :
#             letra = request.POST.get('letra')
#         for i in range(len(palabra)):
#             if letra == palabra[i]

    
    
