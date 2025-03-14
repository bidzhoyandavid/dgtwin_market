from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from django.conf import settings

class Command(BaseCommand):
    help = 'Set up the default Site configuration for django-allauth'

    def handle(self, *args, **options):
        # Get or create the default site
        site, created = Site.objects.get_or_create(
            id=settings.SITE_ID,
            defaults={
                'domain': 'localhost:8000',
                'name': 'DG TWIN MARKET'
            }
        )

        if not created:
            site.domain = 'localhost:8000'
            site.name = 'DG TWIN MARKET'
            site.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully {"created" if created else "updated"} Site configuration'
            )
        ) 