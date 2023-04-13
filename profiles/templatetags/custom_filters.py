from django import template

register = template.Library()


@register.filter(name='attr')
def attr(field, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    attrs = {}
    for arg in arg_list:
        if ':' in arg:
            key, val = arg.split(':')
            attrs[key] = val
        else:
            attrs[arg] = True
    if 'checked' in attrs and attrs['checked'] == 'user_profile':
        attrs['checked'] = getattr(field.field.initial, field.name, False)
        if field.value() == 'on':
            attrs['checked'] = True
    return field.as_widget(attrs=attrs)
