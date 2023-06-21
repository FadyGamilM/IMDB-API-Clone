from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from ...models import Movie
from ...api.serializers import MovieSerializer
from rest_framework import status

# List all movies controller 
class MoviesListView(APIView):
    def get(self, request:Request):
        all_movies = Movie.objects.all()
        serializer = MovieSerializer(all_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# controller class responsible for all actions on a specific movie
class MovieDetailsView(APIView):
    def get(self, request: Request, pk : int):
        try:
            movie = Movie.objects.get(pk = pk)
        except Movie.DoesNotExist:
            return Response(data = {"error": "resource is not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request:Request, pk : int):
        try:
            movie = Movie.objects.get(pk = pk)
        except Movie.DoesNotExist:
            return Response(data = {"error": "resource is not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(instance= movie, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)
        
    def delete(self, request:Request, pk : int):
        try:
            movie = Movie.objects.get(pk = pk)
        except Movie.DoesNotExist:
            return Response(data = {"error": "resource is not found"},status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(data="deleted", status=status.HTTP_204_NO_CONTENT)


# Create a new movie controller 
class MovieCreateView(APIView):
    def post(self, request:Request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        