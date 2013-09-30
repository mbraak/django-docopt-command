DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = (
    'docopt_example',
)

SECRET_KEY = '19a9dfb2b77241ef8d504229d3e11b09'

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