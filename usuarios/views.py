from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

def registro(request):
    form = UserCreationForm(
        request.POST if request.method == "POST" else None
    )
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("iniciar_sesion")
    return render(request, "usuarios/registro.html", {"form": form})

def iniciar_sesion(request):
    form = AuthenticationForm(
        request,
        data=request.POST if request.method == "POST" else None
    )
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("/")
    return render(request, "usuarios/iniciar_sesion.html", {"form": form})