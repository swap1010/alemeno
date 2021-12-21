from django.contrib import admin
from .models import kid, image
from django import forms

# Register your models here.
admin.site.register(kid)


class adminmy(admin.ModelAdmin):
    readonly_fields = ('created_on', "image_tag")
    radio_fields = {"Group": admin.HORIZONTAL}


admin.site.register(image, adminmy)
