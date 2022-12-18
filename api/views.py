from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, generics

from .serializers import PhotoPointSerializer, StatuisPointSerializer, ImageSerializer
from .models import FunctionTurnPointModel, StatusModel, ImageModel

def home(request):
    context = {
        'images': ImageModel.objects.all()
    }
    return render(request, 'index.html', context)


# Status Point Model Views ----------------------------------------------------------------
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def status_point_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        status_point_data = StatusModel.objects.get(id=pk)
    except StatusModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StatuisPointSerializer(status_point_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StatuisPointSerializer(status_point_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = StatuisPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        status_point_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#---------------------------------------------------------------------------------------------------------

# Image Model Views --------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def image_list(request):
    if request.method == 'GET':
        image_data = ImageModel.objects.all()
        serializer = ImageSerializer(image_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def image_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        photo_data = ImageModel.objects.get(id=pk)
    except StatusModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImageSerializer(photo_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ImageSerializer(photo_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        photo_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#---------------------------------------------------------------------------------------------------------


@api_view(['GET', 'POST'])
def turn_point_list(request):

    if request.method == 'GET':
        photo_point_data = FunctionTurnPointModel.objects.all()
        serializer = PhotoPointSerializer(photo_point_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PhotoPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def turn_point_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        photo_point_data = FunctionTurnPointModel.objects.get(id=pk)
    except FunctionTurnPointModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhotoPointSerializer(photo_point_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhotoPointSerializer(photo_point_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = PhotoPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        photo_point_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def make_photos(request):
    """Add new product pages"""
    if request.method == 'POST':
        data = {'turn_point': 1}
        headers = {"Content-Type": "application/json"}
        requests.put('http://localhost:8000/api/turn_point/1', json=data, headers=headers)
        # form = ProductForm(data=request.POST, files=request.FILES)
        # if form.is_valid():
        #     new_product = form.save(commit=False)
        #     new_product.creator = request.user
        #     new_product.save()
        #     return redirect('index')
        return redirect('index')
    else:
        return redirect('index')

def make_two(request):
    """Add new product pages"""
    if request.method == 'POST':
        data = {'turn_point': 2}
        headers = {"Content-Type": "application/json"}
        requests.put('http://localhost:8000/api/turn_point/1', json=data, headers=headers)
        return redirect('index')
    else:
        return redirect('index')

def make_three(request):
    """Add new product pages"""
    if request.method == 'POST':
        data = {'turn_point': 3}
        headers = {"Content-Type": "application/json"}
        requests.put('http://localhost:8000/api/turn_point/1', json=data, headers=headers)
        return redirect('index')
    else:
        return redirect('index')


# def turn_point_button_save(request):
#     # if request.method == 'POST':
#     if  request.GET.get('change_turn'):
#         turn_value = request.POST.get('change_turn')
#         data={'turn_point': turn_value}
#         headers = {"Content-Type": "application/json"}
#         apipath=requests.put('http://localhost:8000/api/photo_point/1/', json=data, headers=headers)
#         # requests.put('http://localhost:8000/api/photo_point/1/', json=data, headers=headers)
#         return render(request, "api/index.html")
#     else:
#         return render(request, "api/index.html")