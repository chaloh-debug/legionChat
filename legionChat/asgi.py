import os
from django.conf import settings
settings.configure()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "legionChat.settings")

import chat.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns


django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "https": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)