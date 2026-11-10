from django.shortcuts import render

# Create your views here.
def bienvenida(request):
    request.session["nombre"] = "Ada"
    nombre = request.session.get("nombre", "visitante") #El primer parámetro es la clave, el segundo es el valor por defecto si no existe
    return render(request, "bienvenida.html", {"nombre": nombre})