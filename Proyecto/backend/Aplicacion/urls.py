from django.urls import path
from . import views
from .views import lista_cursos

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarCurso/', views.registrarCurso, name='registrarCurso'),
    path('edicionCurso/<str:codigo>/', views.edicionCurso, name='edicionCurso'),
    path('editarCurso/', views.editarCurso, name='editarCurso'),
    path('eliminarCurso/<str:codigo>/', views.eliminarCurso, name='eliminarCurso'),
    path('api/cursos/', lista_cursos, name='lista_cursos'),  # API endpoint
]
