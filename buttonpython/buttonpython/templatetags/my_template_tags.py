@register.filter('my_template_tags',my_template_tags)
def at_index(data, index):
    return data[index]
