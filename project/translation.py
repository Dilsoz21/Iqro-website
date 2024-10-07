from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from project.models import Project, Category


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

