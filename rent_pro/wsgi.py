"""
WSGI config for rent_pro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
path = '/home/Rayyan24/Rental_App_Prod/'
if path not in sys.path:
    sys.path.append(path) 
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rent_pro.settings')

application = get_wsgi_application()
