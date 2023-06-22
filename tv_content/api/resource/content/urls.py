from django.urls import path
from .views import ContentCreateApiView, ContentDetailsActionsApiView, ContentListApiView

resource_details_uri = '<int:pk>/'

urlpatterns = [
    path('list/', ContentListApiView.as_view() , name='content_list_action'),
    path(resource_details_uri, ContentDetailsActionsApiView.as_view(), name='content_details_actions'),
    path('new/', ContentCreateApiView.as_view(), name='content_create_action')
]
