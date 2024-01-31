from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from crmapp.models import Record

# Register the Account model
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'email', 'creation_date')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    ordering = ('-creation_date',)
    # readonly_fields = ('user',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Record, RecordAdmin)
