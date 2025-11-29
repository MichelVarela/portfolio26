from django import template

register = template.Library()

@register.filter
def get_form_field(form, field_name):
    """
    Returns the bound field from the form for the given field name.
    Usage: {{ form|get_form_field:field_name }}
    """
    try:
        return form[field_name]
    except KeyError:
        return None
