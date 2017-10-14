from django.apps import apps
from django.contrib import admin

clubsapp = apps.get_app_config('clubsapp')

for model_name, model in clubsapp.models.items():
    admin.site.register(model)