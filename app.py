from django.core.wsgi import get_wsgi_application
import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Todo.settings')

app = get_wsgi_application()
