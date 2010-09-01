#!/usr/bin/env python

import sys
from os.path import dirname, abspath
from django.conf import settings
from django.test.simple import run_tests

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'taggit',
            'taggit_templatetags',
            'taggit_templatetags.tests'            
        ]
    )

def runtests(*test_args):
    if not test_args:
        test_args = ['tests']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])