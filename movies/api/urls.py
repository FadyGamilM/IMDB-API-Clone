from django.urls import path

################################# Function based views ##############################################
# from .func_based_view.views import list_movies, movie_details, create_movie
# urlpatterns = [
#     path('list/', list_movies),
#     path('new/', create_movie),
#     path('<int:pk>/', movie_details)
# ]
#######################################################################################################

################################# Function based views ##############################################
from .class_based_view.views import MovieCreateView, MovieDeleteView, MovieDetailsView, MoviesListView, MovieUpdateView

resource_details_id = '<int:pk>/'

urlpatterns = [
    path('list/', MoviesListView.as_view(), name='movie-list'),
    path('new/', MovieCreateView.as_view(), name='movie-create'),
    path(resource_details_id, MovieDetailsView.as_view(), name='movie-details')
    # path(resource_details_id, MovieUpdateView.as_view(), name='movie-update'),
    # path(resource_details_id, MovieDeleteView.as_view(), name='movie-delete'),
]
#######################################################################################################
