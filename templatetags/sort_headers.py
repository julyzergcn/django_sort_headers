from django import template

register = template.Library()

def table_header(context, headers):
    return {
        'headers': headers,
    }

register.inclusion_tag('sort_headers/table_header.html', takes_context=True)(table_header)
