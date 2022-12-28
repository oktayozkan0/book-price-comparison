from django import template

register = template.Library()

@register.filter("is_text")
def text_field(ob):
    if ob.field.widget.__class__.__name__ == "TextInput":
        return True
    else:
        return False

@register.filter("is_checkbox")
def checkbox_field(ob):
    if ob.field.widget.__class__.__name__ == "CheckboxSelectMultiple":
        return True
    else:
        return False

@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)