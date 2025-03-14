from django.apps import AppConfig


class MarketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'market'

    def ready(self):
        try:
            import market.signals  # noqa
        except ImportError:
            pass
