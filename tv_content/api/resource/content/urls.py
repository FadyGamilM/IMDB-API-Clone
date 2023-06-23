from django.urls import path
from .views import ContentCreateApiView, ContentDetailsActionsApiView, ContentListApiView
from ..review.views import ContentReviewListApiView, ContentReviewDetailsApiView

resource_details_uri = '<int:pk>/'

urlpatterns = [
    path('list/', ContentListApiView.as_view(), name='content_list_action'),
    path(resource_details_uri, ContentDetailsActionsApiView.as_view(),
         name='content_details_actions'),
    path('new/', ContentCreateApiView.as_view(), name='content_create_action'),
    path(resource_details_uri+'reviews', ContentReviewListApiView.as_view(),
         name='content_reviews_list_action'),
    path('<int:content_pk>/reviews/<int:review_pk>',
         ContentReviewDetailsApiView.as_view(), name='content_review_details_actions')
]
