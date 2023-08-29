# def application(env, start_response):
#     start_response('200 OK', [('Content-Type','text/html')])
#     test = 'hello world'
#     return test.encode("utf-8")




import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platform.settings')

application = get_wsgi_application()