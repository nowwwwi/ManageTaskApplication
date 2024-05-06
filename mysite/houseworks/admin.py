from django.contrib import admin
from .models import Work, WorkType, WorkProcess, History


class WorkProcessInline(admin.TabularInline):
    model = WorkProcess
    extra = 3


class WorkAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "pub_date",
        "update_date",
        "work_type"
    ]
    inlines = [WorkProcessInline]


# Register your models here.
admin.site.register(Work, WorkAdmin)
admin.site.register(WorkType)
admin.site.register(WorkProcess)
admin.site.register(History)