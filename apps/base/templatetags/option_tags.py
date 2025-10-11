from django import template

from apps.base.models import Option

register = template.Library()

def get_option(key, default_value="", priority=0):
    obj, _ = Option.objects.get_or_create(key=key, defaults={"value": default_value, "priority": priority})
    return obj.value

@register.simple_tag
def theme_option(key, default="", priority=0):
    return get_option(key, default, priority)