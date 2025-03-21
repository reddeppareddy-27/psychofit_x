import hashlib
from django import template

register = template.Library()

@register.filter
def md5(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()
