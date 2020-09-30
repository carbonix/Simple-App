#!/usr/bin/env python
import os
import sys
django_settings = "DJANGO_SETTINGS_MODULE"
page_project = "page_project.settings"
import_error =  "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
if __name__ == "__main__":
    os.environ.setdefault(django_settings, page_project)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
               import_error
            )
        raise
    execute_from_command_line(sys.argv)
