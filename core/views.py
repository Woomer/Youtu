
from rest_framework import viewsets
from .models import YouTubeChannel, Video, Editor, Approval
from .serializers import YouTubeChannelSerializer, VideoSerializer, EditorSerializer, ApprovalSerializer

class YouTubeChannelViewSet(viewsets.ModelViewSet):
    queryset = YouTubeChannel.objects.all()
    serializer_class = YouTubeChannelSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class EditorViewSet(viewsets.ModelViewSet):
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer

class ApprovalViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
