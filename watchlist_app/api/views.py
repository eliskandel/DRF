from ..models import Movie
# from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response
from .serializers import MovieSerializer


class MovieList(APIView):
    def get(self, request):
        movie=Movie.objects.all()
        serializer=MovieSerializer(movie, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class MovieDetail(APIView):
    def get(self,request,pk):
        try:
            movie=Movie.objects.get(pk=pk)
            serializer=MovieSerializer(movie)
            return Response(serializer.data)
        except:
            return Response({"message":"Not Found"})
    
    def delete(self,request,pk):
        try:
            movie=Movie.objects.get(pk=pk)
            movie.delete()
            return Response({"message":"Deleted"})
        except:
            return Response({"message":"Not Found WitH given Id"})
        
    def put(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message":"Hello"})


# Create your views here.
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies=Movie.objects.all()
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