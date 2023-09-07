from django.shortcuts import render
from .models import EmpData
from .serializers import EmpDataSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class EmpDataView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request,Format=None):
        qdata=EmpData.objects.all()
        serializer=EmpDataSerializer(qdata,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,Format=None):
        serializer=EmpDataSerializer(data=request.data,many=True)
        
        if serializer.is_valid():
            serializer.save()
            result={'messge':'your data is successfully posted'}
            return Response(result,status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
class EmpDataUpdate(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request,pk,Format=None):
        qdata=EmpData.objects.get(pk=pk)
        serializer=EmpDataSerializer(qdata)
        return Response(serializer.data)
    
    def put(self,request,pk,Format=None):
        qdata=EmpData.objects.get(pk=pk)
        serializer=EmpDataSerializer(qdata,data=request.data)
        if serializer.is_valid():
            serializer.save()
            result={'messge':'your data is successfully updated'}
            return Response(result,status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)
    
    def delete(self,rquest,pk,Format=None):
         qdata=EmpData.objects.get(pk=pk)
         qdata.delete()
         result={'messege:your data is successfully deleted'}
         return Response(result)
        
        
        
    