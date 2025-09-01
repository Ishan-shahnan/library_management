
import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Ensure Django is set up
django.setup()

# Collect static files on startup for Vercel
try:
    from django.core.management import call_command
    import sys
    
    # Only collect static files in production (when not in DEBUG mode)
    from django.conf import settings
    if not settings.DEBUG:
        # Create staticfiles directory if it doesn't exist
        import pathlib
        staticfiles_dir = pathlib.Path(settings.STATIC_ROOT)
        staticfiles_dir.mkdir(exist_ok=True)
        
        # Collect static files
        call_command('collectstatic', '--noinput', '--clear', verbosity=0)
except Exception as e:
    print(f"Static files collection failed: {e}")

application = get_wsgi_application()
app = application
