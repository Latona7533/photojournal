
from modeltranslation.translator import register, TranslationOptions
from photojournal .models import Blog

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('genre', 'title', 'description')
