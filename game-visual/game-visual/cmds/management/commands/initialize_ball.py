from django.core.management.base import BaseCommand
from api.models import Ball


class Command(BaseCommand):
    help = 'Initializes a default Ball object in the database.'

    def handle(self, *args, **options):
        Ball.objects.get_or_create(name='DefaultBall',
                                   defaults={'position': {},
                                             'velocity': {},
                                             'speed': 0.0,
                                             'direction': 1})
        self.stdout.write(
                self.style.SUCCESS('Successfully initialized the Ball object'))
