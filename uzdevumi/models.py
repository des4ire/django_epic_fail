from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#class Limiter(models.Model):
#    limited_integer_field = IntegerField(
#        default=1,
#        validators=[
 #           MaxValueValidator(100),
#            MinValueValidator(1)
#        ]
 #    )

class Visit(models.Model):

    student = models.CharField(max_length=100)
    #reason = models.CharField(max_length=140)
    #date_time = models.DateTimeField()
    math = models.IntegerField()
    english = models.IntegerField()
    science=models.IntegerField()
    #average=models.FloatField()