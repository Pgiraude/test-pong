from django.db import models


class Ball(models.Model):
    name = models.CharField(max_length=100, unique=True)
    position = models.JSONField()  # Stores position as a JSON object
    velocity = models.JSONField()  # Stores velocity as a JSON object
    speed = models.FloatField()  # Assuming speed is a floating-point number
    direction = models.IntegerField()  # 1 for positive Z direction, -1 for neg

    def __str__(self):
        return self.name
