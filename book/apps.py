from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "book"
    version = '1.0.1'

    def ready(self):
        print("book app is ready")
        pass  # startup code here
