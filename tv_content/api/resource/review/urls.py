from django.urls import path
from .views import ReviewListApiView, ReviewCreateApiView, ReviewDetailsApiVeiw


urlpatterns = [
    # in my opinion all these urls and their views are useless because we can't create a review without specifying its content, and same for retrieving and other actions, so these endppoints can be for internal working or testing only 
    path('list/', ReviewListApiView.as_view(), name='reviews_list_action'),
    path('new/', ReviewCreateApiView.as_view(), name='reviews_create_action'),
    path('<int:pk>/', ReviewDetailsApiVeiw.as_view(),
         name='reviews_details_actions')
]
