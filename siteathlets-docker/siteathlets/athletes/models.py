from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмены'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.age} лет)'
