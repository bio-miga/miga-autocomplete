from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    name = 'quickstart'
    label = 'quickstart'
    url_prefix = "miga"
    
    def enabled(self, request):
        # Exclude from menus
        return False
