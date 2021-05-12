from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Event(models.Model):
    class StateChoice(models.TextChoices):
        ALA = "Almaty"
        AST = "Nur-Sultan"
        CIT = "Shymkent"
        GUW = "Atyrau"
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, choices=StateChoice.choices, default=StateChoice.ALA)
    zipcode = models.CharField(max_length=10)
    other = models.CharField(max_length=10)
    start_date = models.CharField(max_length=25)
    end_date = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    list_date = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'events'

    def __init__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)






