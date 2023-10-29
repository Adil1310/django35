from django import template

register = template.Library()

@register.filter(name='half_string')
def half_string(value):
    try:
        half = len(value) // 2
        return value[:half]
    except (ValueError, TypeError):
        return value

@register.simple_tag
def split_string(value, separator):
    try:
        return value.split(separator)
    except Exception as e:
        return []

