from django.urls import path


from .views import list_movies, movie_details, create_movie


urlpatterns = [
    path('list/', list_movies),
    path('new/', create_movie),
    path('<int:pk>/', movie_details)
]
