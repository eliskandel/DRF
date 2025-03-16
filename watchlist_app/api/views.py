from ..models import Platform,WatchList
# from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response
from .serializers import WatchListSerializer,PlatformSerializer


class WatchListView(APIView):
    def get(self, request):
        watchList=WatchList.objects.all()
        serializer=WatchListSerializer(watchList, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class WatchListDetailView(APIView):
    def get(self,request,pk):
        try:
            watchList=WatchList.objects.get(pk=pk)
            serializer=WatchListSerializer(watchList)
            return Response(serializer.data)
        except:
            return Response({"message":"Not Found"})
    
    def delete(self,request,pk):
        try:
            watchList=WatchList.objects.get(pk=pk)
            watchList.delete()
            return Response({"message":"Deleted"})
        except:
            return Response({"message":"Not Found WitH given Id"})
        
    def put(self,request,pk):
        watchList=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(watchList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message":"Hello"})



class PlatformView(APIView):
    def get(self, request):
        platform=Platform.objects.all()
        serializer=PlatformSerializer(platform,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class PlatformDetailView(APIView):
    def get(self, request, pk):
        try:
            platform=Platform.objects.get(pk=pk)
            serializer=PlatformSerializer(platform)
            return Response(serializer.data)
        except:
            return Response({"message":"Not ffound"})
    def put(self, request, pk):
        try:
            platform=Platform.objects.get(pk=pk)
            serializer=PlatformSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"message":"Please enter validated data"})
        except:
            return Response({"message":"Not ffound"})
    def delete(self,request,pk):
        try:
            platform=Platform.objects.get(pk=pk)
            platform.delete()
            return Response({"message":"Deleted"})
        except:
            return Response({"message":"Not ffound"})



# Create your views here.
# @api_view(['GET','POST'])
# def WatchList_list(request):
#     if request.method == 'GET':
#         WatchLists=WatchList.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
# @api_view(['GET','PUT','DELETE'])    
# def movie_details(request, pk):
#     if request.method == 'GET':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         try:
#             movie=Movie.objects.get(pk=pk)
#             movie.delete()
#             return Response({"message":"Deleted"})
#         except:
#             return Response({"messagae":"NOT found"},status=status.HTTP_204_NO_CONTENT)