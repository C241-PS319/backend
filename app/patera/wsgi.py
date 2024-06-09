from config.firebase import initialize_firebase_app
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.patera.settings")

initialize_firebase_app()

application = get_wsgi_application()