import logging
import os
import json
import time
import random

from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

logger = logging.getLogger(__name__)

@api_view(['GET','POST'])
def mock_alta_garantia(request):
	time.sleep(3)
	n = random.randint(1,1000)
	response = 	{ 
	  "id_garantizar": request.data['id_garantizar'],
	  "id_fogar": n,
	  "message": "OK"
	}
	return Response(response, status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def mock_actualizacion_garantia(request):
	time.sleep(3)
	n = random.randint(1,1000)
	response = 	{
	  "id_garantizar": request.data['id_garantizar'],
	  "id_fogar": n,
	  "message": "OK"
	}
	return Response(response, status=status.HTTP_201_CREATED)