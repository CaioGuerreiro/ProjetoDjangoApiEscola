
from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer

# Create your views here.

class AlunoViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos e alunas """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    #Exibindo todos os cursos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer