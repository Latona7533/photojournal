from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from accounts.models import Profile


class ProfileAdmin(TranslationAdmin):
    list_display = ( 'username',)

admin.site.register(Profile, ProfileAdmin)