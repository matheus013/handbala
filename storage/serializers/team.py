from rest_framework import serializers

from storage.models.team import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
