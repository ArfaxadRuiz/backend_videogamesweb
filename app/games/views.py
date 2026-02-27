from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Game
from .serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
