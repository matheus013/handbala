from rest_framework import serializers

from storage.models.player import Player


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
