from django.contrib import admin
from .models import prediction
from .models import output

# Register your models here.
admin.site.register(prediction)
admin.site.register(output)