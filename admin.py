from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class {{camel_case_app_name}}Config(AppConfig):
    name = 'apps.{{camel_case_app_name}}'
    verbose_name = _('{{camel_case_app_name}}')