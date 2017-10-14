from django.apps import apps
from django.contrib import admin
from models import company_table

portalapp = apps.get_app_config('portalapp')

for model_name, model in portalapp.models.items():
    admin.site.register(model)

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['company_name', 'id', 'startdate', 'recentdate']
	class Meta:
		model = company_table

