from django.shortcuts import render
from rest_framework.views import APIView
from .models import Travel, Mehmonxona, Klass
from .serializers import KlassSerializer, MehmonxonaSerializer, TravelSerializer
from rest_framework.response import Response
from rest_framework import status


class KlassView(APIView):
    
    
    def get(self, request, pk=None):
        if pk:
            try:
                klass = Klass.objects.get(pk=pk)
                return Response(KlassSerializer(klass).data)
            except:
                return Response({"message": "Klass Not Found"}, status=status.HTTP_404_NOT_FOUND)
            
        klasses = Klass.objects.all()
        return Response(KlassSerializer(klasses, many=True).data)
        
    
    def post(self, request):
        nomi = request.data["nomi"]
        narxi = request.data["narxi"]
        klass = Klass.objects.create(nomi=nomi, narxi=narxi)
        serializer = KlassSerializer(klass)
        return Response(serializer.data)
    
    
    def delete(self, request):
        klass = self.get_object()
        if klass is None:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        klass.delete()
        return Response(status=status.HTTP_404_NO_CONTENT)
    
    
    def put(self, request, pk=None):
        if not pk:
            return Response("Method PUT not allowed", status=status.HTTP_404_NOT_FOUND)
        
        klass = Klass.objects.get(pk=pk)
        serializer = KlassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_klass = serializer.update(klass, serializer.validated_data)
        
        return Response(KlassSerializer(updated_klass).data)
    


class MehmonxonaView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            try:
                mehmonxona = Mehmonxona.objects.get(pk=pk)
                return Response(MehmonxonaSerializer(mehmonxona).data)
            except:
                return Response({"message": "Mehmonxona Not Found"}, status=status.HTTP_404_NOT_FOUND)
            
        mehmonxonas = Mehmonxona.objects.all()
        return Response(MehmonxonaSerializer(mehmonxonas, many=True).data)
    
    
    def post(self, request):
        nomi = request.data["nomi"]
        yulduzlar_soni = request.data["yulduzlar_soni"]
        narxi = request.data["narxi"]
        mehmonxona = Mehmonxona.objects.create(nomi=nomi, yulduzlar_soni=yulduzlar_soni, narxi=narxi)
        serializer = MehmonxonaSerializer(mehmonxona)
        return Response(serializer.data)
    
    
    def delete(self, request):
        mehmonxona = self.get_object()
        if mehmonxona is None:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        mehmonxona.delete()
        return Response(status=status.HTTP_404_NOT_CONTEND)
    
    
    def put(self, request, pk=None):
        if not pk:
            return Response("Method PUT not allowed", status=status.HTTP_404_NOT_FOUND)
        
        mehmonxona = Mehmonxona.objects.get(pk=pk)
        serializer = MehmonxonaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_mehmonxona = serializer.update(mehmonxona, serializer.validated_data)
        
        return Response(MehmonxonaSerializer(updated_mehmonxona).data)
    
    
        
class TravelView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                return Response(TravelSerializer(travel).data)
            except:
                return Response({"message": "Travel Not Found"}, status=status.HTTP_404_NOT_FOUND)
            
        travels = Travel.objects.all()
        return Response(TravelSerializer(travels, many=True).data)
    
    
    def post(self, request):
        nomi = request.data["nomi"]
        izoh = request.data["izoh"]
        muddati = request.data["muddati"]
        narxi = request.data["narxi"]
        klass_id = request.data["klass_id"]
        
        klass = Klass.objects.get(pk=klass_id)
        
        mehmonxona_id = request.data["mehmonxona_id"]
        
        mehmonxona = Mehmonxona.objects.get(pk=mehmonxona_id)
        
        travel = Travel.objects.create(nomi=nomi, izoh=izoh, muddati=muddati, narxi=narxi, klass=klass, mehmonxona=mehmonxona)
        
        serializer = TravelSerializer(travel)
        return Response(serializer.data)        
        
        
    def delete(self, request):
        travel = self.get_object()
        if travel is None :
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND) 
        travel.delete()
        return Response(status=status.HTTP_404_NOT_CONTEND)
     
     
    def put(self, request, pk=None):
        if not pk:
            return Response("Method PUT not allowed", status=status.HTTP_404_NOT_FOUND)
        
        travel = Travel.objects.get(pk=pk)
        serializer = TravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_travel = serializer.update(travel, serializer.validated_data)
        
        return Response(TravelSerializer(updated_travel).data)