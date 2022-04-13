from rest_framework import viewsets

from storage.models.game import Game
from storage.serializers.game import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
