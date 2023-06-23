from django.urls import path
from .views import ContentCreateApiView, ContentDetailsActionsApiView, ContentListApiView
from .views import ContentReviewListApiView, ContentReviewDetailsApiView, ContentReviewCreateApiView

resource_details_uri = '<int:pk>/'

urlpatterns = [
    # list all contents from all types
    path('list/', ContentListApiView.as_view(), name='content_list_action'),
    # get details of specific content | update specific content | delete specific content
    path(resource_details_uri, ContentDetailsActionsApiView.as_view(),
         name='content_details_actions'),
    # create a new content
    path('new/', ContentCreateApiView.as_view(), name='content_create_action'),
    # get all reviews of specific content
    path(resource_details_uri+'reviews', ContentReviewListApiView.as_view(),
         name='content_reviews_list_action'),
    # get specific review of specific content
    path('<int:content_pk>/reviews/<int:review_pk>',
         ContentReviewDetailsApiView.as_view(), name='content_review_details_actions'),
    # crete a review for a specific content
    path('<int:content_pk>/reviews/new/', ContentReviewCreateApiView.as_view(),
         name='content_review_create_action')
]
