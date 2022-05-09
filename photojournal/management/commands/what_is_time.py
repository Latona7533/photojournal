
from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Curr time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write(time)