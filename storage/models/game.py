from django.db import models
import uuid

from storage.models.team import Team


class Game(models.Model):
    hashcode = models.CharField(max_length=255, verbose_name='Chave única')
    appointment = models.DateTimeField(verbose_name='Hora Marcada')
    team_a = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Time A')
    team_b = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Time B')
    gols_a = models.IntegerField(default=0)
    gols_b = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.team_a} x {self.team_b}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Jogo'

    def save(self, *args, **kwargs):
        self.hashcode = uuid.uuid4()
        super(Game, self).save(*args, **kwargs)
