from django.shortcuts import render,reverse,redirect
from .models import order 
from .serializers import  orderSerializer
from rest_framework.response import Response
from rest_framework import status, generics
import datetime







class orderView(generics.CreateAPIView):
    serializer_class = orderSerializer
    queryset = order.objects.all()

    def post(self, request, format=None):
        serializer = orderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # user_id = request.data.get('user_id')
        # print("user_id_API",user_id)
        # queryset = order.objects.filter(user=user_id)
        queryset = order.objects.all()
        print(queryset)
        serializer = orderSerializer(queryset, many=True)
        return Response(serializer.data)



class OrderRetrieveView(generics.CreateAPIView):
    serializer_class = orderSerializer
    queryset = order.objects.all()
    def create(self, request, *args, **kwargs):
        queryset = order.objects.filter(pk=kwargs['pk']).first()
        if queryset:
            serializer = self.serializer_class(queryset)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": False, "data": "Data not found"}, status=status.HTTP_404_NOT_FOUND)


class OrderDetailUpdateView(generics.UpdateAPIView):
    serializer_class = orderSerializer
    def update(self, request, *args, **kwargs):
        queryset = order.objects.filter(pk=kwargs['pk']).first()
        if queryset:
            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": "Data updated successfully"}, status=status.HTTP_201_CREATED)
            return Response({"status": False, "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": False, "data": "Data not found"}, status=status.HTTP_404_NOT_FOUND)



class OrderDetailDeleteView(generics.DestroyAPIView):
    serializer_class = orderSerializer
    def delete(self, request, *args, **kwargs):
        queryset = order.objects.filter(pk=kwargs['pk']).first()
        if queryset:
            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            if serializer.is_valid():
                queryset.delete()
                return Response({"status": True, "data": "Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            return Response({"status": False, "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": False, "data": "Data not found"}, status=status.HTTP_404_NOT_FOUND)










    
    

