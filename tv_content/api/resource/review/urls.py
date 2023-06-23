from django.urls import path
from .views import ReviewListApiView, ReviewCreateApiView, ReviewDetailsApiVeiw


urlpatterns = [
    path('list/', ReviewListApiView.as_view(), name='reviews_list_action'),
    path('new/', ReviewCreateApiView.as_view(), name='reviews_create_action'),
    path('<int:pk>/', ReviewDetailsApiVeiw.as_view(),
         name='reviews_details_actions')
]
