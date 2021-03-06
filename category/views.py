#from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from category.models import Category
from category.serializers import CategorySerializer


@api_view(['GET', 'POST'])
def category_list(request):
    """
    List all snippets, or create a new article.
    """

    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        cat1 = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(cat1)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(cat1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cat1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
