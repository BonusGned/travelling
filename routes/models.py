from django.db import models

from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Route')
    travel_times = models.PositiveIntegerField(verbose_name='Total travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set',
                                  verbose_name='From which city')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='route_to_city_set',
                                verbose_name='To which city')
    trains = models.ManyToManyField('trains.Train', verbose_name='Train list')

    def __str__(self):
        return f'Route: {self.name} from city {self.from_city}'

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['travel_times']
