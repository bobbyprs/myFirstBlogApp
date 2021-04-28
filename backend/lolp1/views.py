from django.shortcuts import render,HttpResponse
from .serializers import ArticleSerializer,UserSerializer
from .models import Article
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView ,action
from rest_framework import request, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.authtoken.models import Token
from django.contrib.messages.storage import default_storage
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .customPermission import IsOwnerOrReadOnly
# Create your views here.




class ArticleViewSet(viewsets.ModelViewSet,IsOwnerOrReadOnly):
    # userid = User.objects.get(pk=request.user.id)
    queryset = Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes =(TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #       user = self.request.user.id
    #       return Article.objects.filter(owner=user)

class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class=UserSerializer

@api_view(['POST'])
def login(request):
    try:
        user=User.objects.get(username=request.data['username'])
    except:
        return Response('user name error')
    if user.check_password(request.data['password']):
        token, _=Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    return Response('Password incorrect',status=status.HTTP_401_UNAUTHORIZED)

# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['myFile']
#     file_name = default_storage.save(file.name,file)
#     return JsonResponse(file_name,safe=True)

# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['myFile']
#     file_name = default_storage.save(file.name,file)

#     return JsonResponse(file_name,safe=False)

    







# class ArticleList(APIView):

#     def get(self,request):
#         articles =Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,)

# class ArticleDetails(APIView):
#     permission_classes = [IsAuthenticated|ReadOnly]
#     def get_object(self, id):
#         try:
#            return Article.objects.get(id = id)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self,request,id):
#         article =self.get_object(id=id)
#         serializer = ArticleSerializer(article,many=True)
#         return Response(serializer.data)

#     def put(self,request,id):
#         article =self.get_object(id=id)
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,id):
#         article =self.get_object(id=id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#####fuctional based api_views################
# def Index(request):
#     return HttpResponse("its working")
# @csrf_exempt
# @api_view(['GET','POST'])
# def article_list(request):

#     if request.method =='GET':
#         articles =Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# # @csrf_exempt
# @api_view(['GET','PUT','DELETE'])
# def article_details(request,pk):
#     try:
#         article =Article.objects.get(pk=pk)
#     except Article.DoseNotExist:
#         return Response(status=status.)

#     if request.method =='GET':
#            serializer = ArticleSerializer(article)
#            return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)