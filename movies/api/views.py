from django.shortcuts import render
from ..models import Movie
from .serializers import MovieSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

############ Before serializer ###################
# def list_movies(req):
#     # define a query set
#     all_movies = Movie.objects.all()

#     # convert the query set result to a python dictionary
#     data = {
#         'movies': list(all_movies.values())
#     }

#     # convert python dictionary to json format
#     return JsonResponse(data=data)
####################################################


@api_view(http_method_names=["GET"])
def list_movies(request: Request):
    # all movies as a query set
    all_movies = Movie.objects.all()
    # serialize the data from normal python object to a value-ready-to-be-mapped-to-sql
    serializer = MovieSerializer(all_movies, many=True)
    # return the response
    return Response(serializer.data)


@api_view(http_method_names=["POST"])
def create_movie(request: Request):
    # get the data from the request of the user 
    serializer = MovieSerializer(data = request.data)
    print(f"serializer from POST request after serializing the user equest => \t \t \n {serializer}")
    if serializer.is_valid():
        serializer.save()
        # return the persisted and serialized data that we returned from the serializer.create method 
        return Response(serializer.data)
    else:
        return Response(serializer.errors)    

@api_view(http_method_names=["GET"])
def movie_details(request : Request, pk: int):
    # get specific movie
    found_movie = Movie.objects.get(pk=pk)
    # serialize it
    serializer = MovieSerializer(found_movie)
    # return the response
    return Response(serializer.data)
