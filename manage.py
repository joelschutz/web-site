#!/usr/bin/env python
<<<<<<< HEAD
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_site.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
=======
"""Django's command-line utility for administrative tasks."""
import os
import sys
from umafoto_ae import cleaner


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    cleaner.jsons_cleaner()
    main()
>>>>>>> 74158fa133f790eef2dbaacc7130963fa5c60e20
