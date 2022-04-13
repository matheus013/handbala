from django.db import models

from storage.models.team import Team


class Player(models.Model):
    CHOICES_POSITION = [
        (1, 'Armador direita'),
        (2, 'Ponta direita'),
        (3, 'Armador esquerda'),
        (4, 'Ponta esquerda'),
        (5, 'Centro'),
        (6, 'Pivo'),
        (7, 'Goleiro'),
    ]

    name = models.CharField(max_length=100, verbose_name='Nome')
    number = models.IntegerField(verbose_name='Número')
    position = models.IntegerField(choices=CHOICES_POSITION, verbose_name='Posição')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Time')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'

    def save(self, *args, **kwargs):
        super(Player, self).save(*args, **kwargs)
