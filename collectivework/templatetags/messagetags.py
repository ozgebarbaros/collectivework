from django import template

register = template.Library()

@register.simple_tag
def unread_messages(user):
    return user.received_messages.inbox_unread_count(1)
