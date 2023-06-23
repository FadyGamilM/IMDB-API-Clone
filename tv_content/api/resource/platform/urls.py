
from django.urls import path
from .views import StreamingPlatformCreateApiView, StreamingPlatformDetailsActionsApiView, StreamingPlatformListApiView

resource_details_uri = '<int:pk>/'

urlpatterns = [
    path('list/', StreamingPlatformListApiView.as_view(),
         name='platform_list_action'),
    path(resource_details_uri, StreamingPlatformDetailsActionsApiView.as_view(
    ), name='platform_details_actions'),
    path('new/', StreamingPlatformCreateApiView.as_view(),
         name='platform_create_action')
]
