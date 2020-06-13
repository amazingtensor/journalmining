#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# WHAT IT CAN DO...
# runserver: Starts a lightweight development Web server (dev) on the local machine. By default, the server runs on port 8000 on the IP address 127.0.0.1.

import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miningjournal.settings')
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
    main()
