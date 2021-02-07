"""
WSGI config for home project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/school-project')
sys.path.append('/var/www/school-project/home')

# Replace the Python version in the line below as needed 
sys.path.append('/var/www/school-project/school-project-env/lib/python3.8/site-packages') 
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "home.settings") 

try: 
    application = get_wsgi_application() 
except Exception: 
    # Error loading applications 
    if 'mod_wsgi' in sys.modules: 
        traceback.print_exc() 
        os.kill(os.getpid(), signal.SIGINT) 
        time.sleep(2.5)
