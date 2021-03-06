from django.contrib import admin

from htk.apps.prelaunch.models import PrelaunchSignup

class PrelaunchSignupAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'site',
        'created_on',
        'email',
    )

    list_filter = (
        'site',
    )

admin.site.register(PrelaunchSignup, PrelaunchSignupAdmin)
