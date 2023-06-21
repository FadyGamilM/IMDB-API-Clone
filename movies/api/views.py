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
def list_movies(request):
    # all movies as a query set
    all_movies = Movie.objects.all()
    # serialize the data
    serializer = MovieSerializer(all_movies, many=True)
    # return the response
    return Response(serializer.data)


@api_view(http_method_names=["GET"])
def movie_details(request, pk: int):
    # get specific movie
    found_movie = Movie.objects.get(pk=pk)
    # serialize it
    serializer = MovieSerializer(found_movie)
    # return the response
    return Response(serializer.data)
