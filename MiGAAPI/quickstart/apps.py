from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    name = 'quickstart'
    label = 'quickstart'
    url_prefix = "miga"
    
    def enabled(self, request):
        # Exclude from menus
        return False

    def ready(self) -> None:
        from MiGAAPI import queue_settings_calculators  # noqa
