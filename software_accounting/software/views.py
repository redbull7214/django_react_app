from django.core.cache import cache
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SoftwareSerializer
from .services import (
    create_software,
    delete_software,
    get_software_by_id,
    get_software_list,
    update_software,
)


class SoftwareList(APIView):
    """Api for get and post methods."""

    permission_classes = (IsAuthenticated,)

    # def get(self, request: Request) -> Response:
    #     if 'software' in cache:
    #         data=cache.get('software')
    #         print('from cache')
    #     else:
    #         data = get_software_list()
    #         results = [software.to_json() for software in data]
    #         cache.set('software', results)
    #         print('from db')
    #     data = get_software_list()
    #     serializer = SoftwareSerializer(data, many=True)
    #     return Response(serializer.data)
    
    def get(self, request: Request) -> Response:
        data = get_software_list()
        serializer = SoftwareSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = SoftwareSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_software(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class SoftwareDetail(APIView):
    """Api for put and delete methods."""

    permission_classes = (IsAuthenticated,)

    def put(self, request: Request, id: int) -> Response:
        software = get_software_by_id(id=id)
        serializer = SoftwareSerializer(software, data=request.data)
        serializer.is_valid(raise_exception=True)
        update_software(software, serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request: Request, id: int) -> Response:
        software = get_software_by_id(id=id)
        delete_software(software)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogoutView(APIView):
    """Api for logout users."""

    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)


