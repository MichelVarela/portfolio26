from django import template
from base.models import Menu

register = template.Library()

@register.inclusion_tag('tags/menu.html', takes_context=True)
def menu(context):
    return {
        'menu': Menu.objects.all(),
        'request': context['request'],
    }