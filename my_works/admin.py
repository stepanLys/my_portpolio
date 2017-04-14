from django.contrib import admin
from .models import *


class WorkImagInline(admin.TabularInline):
    model = WorkImage
    extra = 0


class WorkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Work._meta.fields]
    inlines = [WorkImagInline]

    exclude = ['']

    class Meta:
        model = Work


admin.site.register(Work, WorkAdmin)


class WorkImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WorkImage._meta.fields]

    exclude = ['']

    class Meta:
        model = WorkImage


admin.site.register(WorkImage, WorkImageAdmin)