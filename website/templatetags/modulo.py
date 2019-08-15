from django import template

register = template.Library()


@register.filter(name='modulo')
def modulo(divisor, divident=3):
    return divisor % divident
