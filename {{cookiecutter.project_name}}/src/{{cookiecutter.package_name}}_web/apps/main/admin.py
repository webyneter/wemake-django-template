from django.contrib import admin

from {{ cookiecutter.package_name }}_web.apps.main.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin[BlogPost]):
    """Admin panel example for ``BlogPost`` model."""
