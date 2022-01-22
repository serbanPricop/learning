from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from drf.models import Bicyle
from drf.serializers import BicyleSerializer


# Create your views here.


@csrf_exempt
@api_view(["GET", 'POST'])
def bicyle_list(request, format=None):
    """
    List of all bicycles or create new instance
    """

    if request.method == "GET":
        bicycles = Bicyle.objects.all()
        serializer = BicyleSerializer(bicycles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BicyleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['DELTE', 'PUT', "GET"])
def bicycle_detail(request, pk, format=None):
    """
    Retrieve, update or delete an instance of Bicycle
    """

    try:
        bicycle = Bicyle.objects.get(pk=pk)
    except Bicyle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BicyleSerializer(bicycle)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BicyleSerializer(bicycle, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        bicycle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

