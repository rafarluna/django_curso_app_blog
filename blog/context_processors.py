# main/context_processors.py
from django.conf import settings
from .models import Category

def all_global(request):
    kwargs = {
        'company_name': settings.SETTING_COMPANY_NAME,
        'CATEGORIES': Category.objects.all()
    }
    return kwargs