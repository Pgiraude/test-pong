from rest_framework import serializers
from .models import Ball


class BallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ball
        fields = ["name", "position", "velocity", "speed", "direction"]

