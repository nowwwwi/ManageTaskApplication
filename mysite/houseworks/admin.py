from django.contrib import admin
from .models import Work, IntervalType, HashTag, WorkProcess, History


class WorkProcessInline(admin.TabularInline):
    model = WorkProcess
    extra = 3


class WorkAdmin(admin.ModelAdmin):
    """"""
    list_display = [
        "name",
        "pub_date",
        "update_date",
    ]
    inlines= [WorkProcessInline]


# Register your models here.
admin.site.register(Work, WorkAdmin)
admin.site.register(HashTag)
admin.site.register(IntervalType)
admin.site.register(WorkProcess)
admin.site.register(History)
