from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import House
from .serializers import HouseSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def HouseView_List(request):
    
    if request.method == 'GET' :
        
        if request.query_params == {}:
            houses = House.objects.all()
            serializer = HouseSerializer(houses , many = True)
            return Response(serializer.data)
        else:
            
            filters = {}
            
            if 'area' in request.query_params:
                filters['area'] = request.query_params['area']

            if 'price' in request.query_params:
                filters['price'] = request.query_params['price']

            if 'state' in request.query_params:
                filters['state'] = request.query_params['state']
           
            if 'city' in request.query_params:
                filters['city'] = request.query_params['city']
           
            if 'is_available' in request.query_params:
                filters['is_available'] = request.query_params['is_available']
           
            if 'views' in request.query_params:
                filters['views'] = request.query_params['views']   
            
            houses = House.objects.filter(**filters)
            
            serializer = HouseSerializer(houses , many=True)
            if serializer.data == []:
                return Response(status= status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.data)
            
    elif request.method == 'POST':
        serializer = HouseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET','PUT','DELETE'])
def HouseView_pk(request , id1):
    try:
        house = House.objects.get(id = id1)
    except House.DoesNotExist :
        return Response(status= status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = HouseSerializer(house)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = HouseSerializer(house , data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data , status= status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        house.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)






    
