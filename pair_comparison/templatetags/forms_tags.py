from django.template import Library

register = Library()

@register.filter(name='dim_form')
def dim_form(form, dim):
    return form[dim]

@register.filter(name='dim_help')
def dim_help(form, dim):
    return form[dim].help_text