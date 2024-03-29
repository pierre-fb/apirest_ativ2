from django.shortcuts import render
from appAutor.models import Autor
from appAutor.serializers import AutorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
@api_view(['GET','POST'])

def autor_list(request):
    if request.method == 'GET':
        autor = Autor.objects.all()
        serializer = AutorSerializer(autor,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=satus.HTTP_400_BAD_REQUEST)