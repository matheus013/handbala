from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Time'
        verbose_name_plural = 'Time'

    def save(self, *args, **kwargs):
        super(Team, self).save(*args, **kwargs)
