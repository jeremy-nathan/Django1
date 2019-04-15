from django import template

register=template.Library()

# Another way to register filter

@register.filter(name='cut')
def cutout(value,arg):
    #Cuts out values of 'arg' from the string
    return value.replace(arg,'')

# register.filter('cut', cut)
#               'TAG', FUNCTION NAME
