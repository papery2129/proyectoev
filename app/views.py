from django.shortcuts import render
from app.models import comentarios
from .import forms

# Create your views here.

def index(request):
    my_context = {
        'username': 'Hola desde views.py'
    }
    return render(request, 'proyectoev/index.html', context=my_context)

def form_user_view(request):
    form = forms.FormUser()

    #print(request.method)
    if request.method == 'POST':
        form = forms.FormUser(request.POST)
        if form.is_valid():
            print("VALIDADO!")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Email: ", form.cleaned_data['email'])
            print("fecha: ", form.cleaned_data['fecha'])
            print("Text: ", form.cleaned_data['text'])
            comment = comentarios.objects.get_or_create(nombre=form.cleaned_data['nombre'],
                                                     email=form.cleaned_data['email'],
                                                     fecha=form.cleaned_data['fecha'],
                                                     text=form.cleaned_data['text'])[0]
            comment.save()


    return render(request, 'proyectoev/formulario.html', {'form' : form})

def tabla(request):
    com_list = comentarios.objects.order_by('fecha')
    my_context = {
        'coment' : com_list
        }
    return render(request, 'proyectoev/tabla_com.html', context= my_context)

def acerca(request):
    return render(request, 'proyectoev/acerca.html')

def seg(request):
    return render(request, 'proyectoev/seguns.html')