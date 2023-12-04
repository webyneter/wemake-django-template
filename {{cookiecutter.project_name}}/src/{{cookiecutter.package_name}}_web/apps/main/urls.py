from django.urls import path

from {{ cookiecutter.package_name }}_web.apps.main.views import index

app_name = 'main'

urlpatterns = [
    path('hello/', index, name='hello'),
]
