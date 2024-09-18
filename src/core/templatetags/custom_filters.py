from django import template

register = template.Library()


# this filter is using for right displaying YouTube video on front
@register.filter
def youtube_embed_url(url):
    return url.replace("watch?v=", "embed/").split("&")[0]


# this filter is using for diagrams in dashboard
@register.filter
def zip_lists(a, b):
    return zip(a, b)

