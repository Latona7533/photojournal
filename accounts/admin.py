from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from accounts.models import Profile


class ProfileAdmin(TranslationAdmin):
    list_display = ('title', 'text',)

admin.site.register(Profile, ProfileAdmin)