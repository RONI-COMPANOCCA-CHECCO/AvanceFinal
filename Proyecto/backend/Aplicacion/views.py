from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response

# API endpoint para obtener la lista de cursos
@api_view(['GET'])
def lista_cursos(request):
    cursos = Curso.objects.all()
    data = [{"id": curso.id, "codigo": curso.codigo, "nombre": curso.nombre, "creditos": curso.creditos} for curso in cursos]
    return Response(data)

# Vista para la página principal que lista los cursos
def home(request):
    cursosListados = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursosListados})

# Vista para registrar un nuevo curso
def registrarCurso(request):
    if request.method == "POST":
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos = request.POST['numCreditos']

        curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
        messages.success(request, 'Curso registrado exitosamente!')
    return redirect('/')

# Vista para la edición de un curso existente
def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

# Vista para actualizar los datos de un curso existente
def editarCurso(request):
    if request.method == "POST":
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos = request.POST['numCreditos']

        curso = Curso.objects.get(codigo=codigo)
        curso.nombre = nombre
        curso.creditos = creditos
        curso.save()
        messages.success(request, 'Curso actualizado exitosamente!')
    return redirect('/')

# Vista para eliminar un curso existente
def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, 'Curso eliminado exitosamente!')
    return redirect('/')
