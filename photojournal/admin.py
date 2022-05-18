from django.contrib import admin
from django.contrib.admin import ModelAdmin
from photojournal.models import Blog, Theme
from modeltranslation.admin import TranslationAdmin

def change_genre(modeladmin, request, queryset):
    queryset.update(genre='GM')
change_genre.short_description = "Change genre for some posts"

@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ('title', 'genre', 'description', 'slug')
    search_fields = ('genre',)
    actions = [change_genre]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Theme)
