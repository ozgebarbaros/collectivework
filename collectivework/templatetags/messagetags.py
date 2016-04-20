from django import template

register = template.Library()

@register.simple_tag
def unread_messages(user):
    #return user.messages_set.filter(read=False).count()
    return user.received_messages.inbox_unread_count(1) 
