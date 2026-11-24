from django.shortcuts import render

# Create your views here.

def sesion(request):
    # Initialize the context dictionary
    context = dict()

    # Check if there are previously stored names
    if request.session.get('nombres'):
        context = {
            'nombre': request.session.get('nombres')
        }

    # Check POST
    if request.method == 'POST':

        # Get the name form (user)
        nombre = request.POST.get('nombre', '')

        #stored names from the session, Add a new name to list, Save names in session.
        nombres = request.session.get('nombres', '')
        nombres += nombre + '\n'
        request.session['nombres'] = nombres

        # current number of visits (sesion), Increase the visit counter by one, Save visit counter in the session
        visitas = request.session.get('visitas', 0)
        visitas += 1
        request.session['visitas'] = visitas

        # Update the context
        context = {
            'nombre': nombres,
            'visitas': visitas,
        }

    # Render the HTML template and pass the context
    return render(request, 'ejemplo.html', context)


