
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import YouTubeChannelViewSet, VideoViewSet, EditorViewSet, ApprovalViewSet

router = DefaultRouter()
router.register(r'channels', YouTubeChannelViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'editors', EditorViewSet)
router.register(r'approvals', ApprovalViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
