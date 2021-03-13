from django.contrib import admin

from trains.models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    list_display_links = ('name',)
    list_editable = ('travel_time',)