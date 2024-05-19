from django.contrib import admin
from .models import Work, HashTag, WorkProcess, History, Schedule, WorkSchedule, WorkHashtag


class Inlines():
    class WorkProcess(admin.TabularInline):
        model = WorkProcess
        extra = 3


    class WorkSchedule(admin.TabularInline):
        model = WorkSchedule
        extra = 3

    class WorkHashtag(admin.TabularInline):
        model = WorkHashtag
        extra = 3

class WorkAdmin(admin.ModelAdmin):
    """"""
    list_display = [
        "id",
        "name",
        "pub_date",
        "update_date",
        "next_execute_date",
    ]

    inlines= [
        Inlines.WorkProcess,
        Inlines.WorkSchedule,
        Inlines.WorkHashtag,]


class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "pub_date",
        "update_date",
    ]


class HistoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "work",
        "pub_date",
    ]


class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "work",
        "schedule",
        "pub_date",
        "update_date",
    ]

# Register your models here.
admin.site.register(Work, WorkAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(HashTag)
admin.site.register(WorkProcess)
admin.site.register(History, HistoryAdmin)

# Middle models.
admin.site.register(WorkSchedule, WorkScheduleAdmin)
