from django.apps import AppConfig


class NeighborappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'neighborapp'
    
    def ready(self):
        import neighborapp.signals
    
