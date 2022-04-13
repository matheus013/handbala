from rest_framework import viewsets

from storage.models.team import Team
from storage.serializers.team import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
