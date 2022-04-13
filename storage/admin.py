from django.contrib import admin

# Register your models here.
from storage.models.game import Game
from storage.models.player import Player
from storage.models.team import Team

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Game)
