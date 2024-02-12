import json
from django.forms.models import model_to_dict
#from django.http import JsonResponse, HttpResponse
from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def api_home(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        data=serializer.data
        return Response(data)
    return Response({"invalid": "not good data"}, status=400)