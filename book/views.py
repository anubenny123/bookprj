from django.shortcuts import render
from book.models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from book.serializres import Bookseializer
from rest_framework import authentication,permissions
# Create your views here.

class BookView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        qs=Book.objects.all()
        serializer=Bookseializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializers=Bookseializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        else:
            return Response(data=serializers.errors)

class BookDetailView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Book.objects.get(id=id)
        serializer=Bookseializer(qs)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Book.objects.get(id=id)
        serializer=Bookseializer(data=request.data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Book.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"})
