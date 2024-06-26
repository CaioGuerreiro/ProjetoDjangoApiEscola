
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, AlunoSerializerV2, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.response import Response

# Create your views here.

class AlunoViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos e alunas """
    queryset = Aluno.objects.all()
   
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    #Exibindo todos os cursos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() +id
            return response
   
    

class MatriculaViewSet(viewsets.ModelViewSet):
    #Exibindo todas as matriculas
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    #especifica os métodos que podem ser usados
    http_method_names = ['get','post','path','put']
   


class ListaMatriculaAluno(generics.ListAPIView):
    #litando as matriculas dos alunos
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer
  
    

class ListaAlunosMatriculados(generics.ListAPIView):
    #Listando alunos e alunas matriculados em um curso
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    
   