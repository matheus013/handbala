from rest_framework import viewsets

from storage.models.player import Player
from storage.serializers.player import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
