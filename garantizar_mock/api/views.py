import logging
import os
import time

from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
@csrf_exempt
def mock_resultado_garantias(request):
	time.sleep(3)
	data = request.data
	response = {"status": "OK", "id_transaccion_recibida": data['id_transaccion']}
	return Response(response, status=status.HTTP_200_OK)
