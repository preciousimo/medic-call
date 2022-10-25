from django.contrib import admin
from base.models import Patient, Support
from django.utils.html import format_html

# PATIENT
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'age', 'gender', 'created_at']
    search_fields = ['name', 'phone', 'email', 'age']
    list_filter = ['gender']
    list_per_page = 10

admin.site.register(Patient, PatientAdmin) 

# SUPPORT
class SupportAdmin(admin.ModelAdmin):
    list_filter = ['situation']
    list_display = ['user', 'reason', 'option', 'created_at', 'status', '_']
    search_fields = ['user', 'reason', 'option']
    list_per_page = 10

    # Function to change the icons (Done - Pending)
    def _(self, obj):
        if obj.situation == 'Done':
            return True
        else:
            return False

    _.boolean = True

    # Function to color the text (Done - Pending)
    def status(self, obj):
        if obj.situation == 'Done':
            color = '#28a745'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation))

    status.allow_tags = True

admin.site.register(Support, SupportAdmin)