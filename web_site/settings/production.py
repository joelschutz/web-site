from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [
    'www.joelschutz.com.br',
    'joelschutz.com.br',
    'localhost',
    '127.0.0.1',
    'joelschutz.herokuapp.com'
    ]

try:
    from .local import *
except ImportError:
    pass
