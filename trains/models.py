from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Train number')
    travel_time = models.PositiveIntegerField(verbose_name='Travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set',
                                  verbose_name='From which city')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='to_city_set',
                                verbose_name='To which city')

    def __str__(self):
        return f'Train number: {self.name} from city {self.from_city}'

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        ordering = ['travel_time']

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Change arrival city')
        qs = Train.objects.filter(from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time).exclude(
            pk=self.pk)
        if qs.exists():
            raise ValidationError('Change the travel time')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)