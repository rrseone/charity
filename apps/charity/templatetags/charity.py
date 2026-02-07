from django import template

register = template.Library()

@register.filter
def absolute(uri, request):
    return request.build_absolute_uri(uri)
