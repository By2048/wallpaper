# coding=utf-8
import logging

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def get_six_disply(value):
    logging.info(value)
    six = {
        '-1': '中性',
        '0': '女性',
        '1': '男性'
    }
    try:
        return six[value]
    except Exception as e:
        logging.error(e)
        return value
