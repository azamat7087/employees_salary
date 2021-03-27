from django.contrib import admin
from .models import *
# Register your models here.


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'days', 'days_skipped', 'added_time', 'last_updated',)
    list_display_links = ('name', 'salary', 'id',)
    search_fields = ('name',)
    readonly_fields = ()
    ordering = ('-salary',)
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(Employee, EmployeesAdmin)


