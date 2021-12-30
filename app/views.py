from django.shortcuts import render
from rest_framework import generics 
from rest_framework.response import Response 
from .serializers import ReadingMemoSerializer
from .models import ReadingMemo

# Create your views here.

class ReadingMemoCreate(generics.CreateAPIView):
    queryset = ReadingMemo.objects.all() 
    serializer_class = ReadingMemoSerializer

class ReadingMemoList(generics.ListAPIView):
    queryset = ReadingMemo.objects.all()
    serializer_class = ReadingMemoSerializer

class ReadingMemoListDetail(generics.RetrieveAPIView):
    queryset = ReadingMemo.objects.all() 
    serializer_class = ReadingMemoSerializer

class ReadingMemoUpdate(generics.RetrieveUpdateAPIView):
    queryset = ReadingMemo.objects.all()
    serializer_class = ReadingMemoSerializer 

class ReadingMemoDestroy(generics.DestroyAPIView):
    queryset = ReadingMemo.objects.all()
    serializer_class = ReadingMemoSerializer 