from django.contrib import admin
from .models import Item
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Item)

