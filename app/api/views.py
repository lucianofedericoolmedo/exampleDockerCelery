# -*- coding: utf-8 -*-

import logging
import os
import json

from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_406_NOT_ACCEPTABLE
)

from . import custom_permissions, garantia_service, garantia_checker_service

logger = logging.getLogger(__name__)


#################### API ####################
@csrf_exempt
@api_view(['POST'])
@permission_classes((custom_permissions.GarantizarPermission,))
def alta_garantias(request, format=None):
    garantias_dict = request.data

    invalidas = garantia_checker_service.errores_en_campos_en_alta(garantias_dict)
    if len(invalidas) > 0:
        return Response(invalidas, status=status.HTTP_406_NOT_ACCEPTABLE)

    try:
        garantia_service.check_broker_connection()
    except RuntimeError as r:
        logger.error(r)
        return Response('Error: servicio no disponible', status=status.HTTP_409_CONFLICT)
    response_data = garantia_service.post_encolar_garantias(garantias_dict)
    return Response(response_data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((custom_permissions.GarantizarPermission,))
def actualizacion_garantias(request, format=None):
    garantias_dict = request.data

    invalidas = garantia_checker_service.errores_en_campos_en_actualizacion(garantias_dict)
    if len(invalidas) > 0:
        return Response(invalidas, status=status.HTTP_406_NOT_ACCEPTABLE)

    try:
        garantia_service.check_broker_connection()
    except RuntimeError as r:
        logger.error(r)
        return Response('Error: servicio no disponible', status=status.HTTP_409_CONFLICT)

    response_data = garantia_service.put_encolar_garantias(garantias_dict)
    return Response(response_data, status=status.HTTP_200_OK)


#################### Login ####################

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


#################### For test purpose only ####################

@csrf_exempt
@api_view(["GET"])
@permission_classes((custom_permissions.GarantizarPermission,))
def sample_secure_garantizar(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_secure_without_perms(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)