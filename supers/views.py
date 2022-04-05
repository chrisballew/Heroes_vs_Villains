from rest_framework.decorators import api_view
from .models import Super
from .serializers import SuperSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        super = Super.objects.all()
        serializer = SuperSerializer(super,many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def super_detail(request,pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data, status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = SuperSerializer(super,data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
    if request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)