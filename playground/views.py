from urllib import response
from django.shortcuts import render
from .models import Data
from .serializers import DataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def item(request):
    if request.method == "GET":
        items = Data.objects.all()
        serializer = DataSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data added successfully")

        return Response("Failed to add data")

    return Response("Enter a valid endpoints")


@api_view(['GET', 'PUT', 'DELETE'])
def action(request, pk):
    item = Data.objects.get(id=pk)
    if request.method == "GET":

        serializer = DataSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = DataSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data edited successfully")

        return Response("Failed to edit data")

    elif request.method == "DELETE":
        item.delete()
        return Response("Data deleted successfully")

# Create your views here.
