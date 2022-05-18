
from modeltranslation.translator import register, TranslationOptions

from accounts.models import Profile
from photojournal .models import Blog


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('genre', 'title', 'description')

@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('username',)