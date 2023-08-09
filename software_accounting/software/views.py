from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import SoftwareSerializer
from .models import Software
from rest_framework.request import Request
from rest_framework.response import Response
from .services import create_software, get_software_list, get_software_by_id, update_software, delete_software
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.core.cache import cache
class SoftwareList(APIView):

    
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request)-> Response:
        # if 'software' in cache:
        #     data=cache.get('software')
        #     print('from cache')
        # else:            
        #     data = get_software_list()
        #     results = [software.to_json() for software in data]
        #     cache.set('software', results)
        #     print('from db')
        data = get_software_list()
        serializer = SoftwareSerializer(data, many=True)
        return Response(serializer.data)
    def post(self, request: Request)-> Response:
        serializer = SoftwareSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_software(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
    
class SoftwareDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request: Request, id: int)-> Response:
        software = get_software_by_id(id=id)
        serializer = SoftwareSerializer(software, data=request.data)
        serializer.is_valid(raise_exception=True)
        update_software(software, serializer.validated_data)
        return Response(status=status.HTTP_200_OK)
    def delete(self, request: Request, id: int)-> Response:
        software = get_software_by_id(id=id)
        delete_software(software)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request: Request)-> Response:
        

        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)


# @api_view(['PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def software_detail(request: Request, id:int) -> Response:
    
#     software = get_software_by_id(id=id)
#     if request.method == 'PUT':
#         serializer = SoftwareSerializer(software, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         update_software(software, serializer.validated_data)
#         return Response(status=status.HTTP_200_OK)
        
#     elif request.method == 'DELETE':
#         delete_software(software)
#         return Response(status=status.HTTP_204_NO_CONTENT)
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def software_list(request: Request) -> Response:
#     if request.method == 'GET':
#         data = get_software_list()
#         serializer = SoftwareSerializer(data, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SoftwareSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         create_software(**serializer.validated_data)
#         return Response(status=status.HTTP_201_CREATED)
        



# class HomeView(APIView):
     
#     permission_classes = (IsAuthenticated, )
#     def get(self, request):
#         content = {'message': 'Welcome to the JWT uthentication page using React Js and Django!'}
#         return Response(content)

# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def post(self, request):
        
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)