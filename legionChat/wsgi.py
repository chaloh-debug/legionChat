import os
from django.conf import settings
settings.configure()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "legionChat.settings")
import django
django.setup()
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
