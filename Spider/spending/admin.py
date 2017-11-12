from django.contrib import admin

from .models import Shopping
from .models import Article

# Register your models here.
admin.site.register(Shopping)
admin.site.register(Article)