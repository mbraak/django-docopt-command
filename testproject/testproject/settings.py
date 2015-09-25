DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = (
    'docopt_example',
)

SECRET_KEY = 'secret'

DATABASES = dict(
    default=dict(
        ENGINE='django.db.backends.sqlite3',
        NAME='example.db',
        USER='',
        PASSWORD='',
        HOST='',
        PORT='',
    )
)

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'testproject.urls'
