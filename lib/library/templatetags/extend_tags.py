from django import template
from ..models import Pic, Message
register = template.Library()


@register.simple_tag
def get_pic():
    hot = Pic.objects.all().order_by('index')
    return hot


@register.simple_tag
def get_txt():
    txt = Message.objects.all()
    return txt
