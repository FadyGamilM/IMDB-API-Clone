from django.urls import path


from .views import list_movies, movie_details


urlpatterns = [
    path('list/', list_movies),
    path('<int:pk>/', movie_details)
]
