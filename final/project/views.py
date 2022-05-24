from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializer import BookSerializer, JournalSerializer, UserSerializer 
from .models import Book, Journal
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class JournalViewSet(viewsets.ModelViewSet):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@api_view(['POST', 'GET'])
def sign_up(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['GET'])
# def get_user(request, username):
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist as e:
#         return Response({'error': str(e)})

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


