from rest_framework import serializers

from storage.models.game import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
