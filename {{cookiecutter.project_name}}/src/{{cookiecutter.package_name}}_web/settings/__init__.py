"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings
https://sobolevn.me/2017/04/managing-djangos-settings

To change settings file:
`ENVIRONMENT=production python manage.py runserver`
"""

from environ import Env
import django_stubs_ext
from split_settings.tools import include, optional

# Monkeypatching Django, so stubs will work for all generics,
# see: https://github.com/typeddjango/django-stubs
django_stubs_ext.monkeypatch()

env = Env()

# Managing environment via `ENVIRONMENT` variable:
ENVIRONMENT = env("ENVIRONMENT")

_base_settings = (
    'components/common.py',
    'components/logging.py',
    'components/csp.py',
    'components/caches.py',

    # Select the right env:
    f'environments/{ENVIRONMENT}.py',

    # Optionally override some settings:
    optional('environments/local.py'),
)

# Include settings:
include(*_base_settings)
