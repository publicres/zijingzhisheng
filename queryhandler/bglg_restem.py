#-*- coding:utf-8 -*-
import random
import string
import datetime

from queryhandler.handler_check_templates import *
from queryhandler.weixin_reply_templates import *
from queryhandler.weixin_text_templates import *

def bl_check_book(msg):
    return handler_check_text_header(msg, ['抢', 'depechez'])

def bl_check_info_trivial(msg):
    return handler_check_text_header(msg, ['团委资讯', 'tinfoprantez'])

def bl_check_info_nearby(msg):
    return handler_check_text_header(msg, ['近期资讯', 'ninfoprantez'])

def bl_check_info_art(msg):
    return handler_check_text_header(msg, ['文艺演出', 'ainfoprantez'])

def bl_check_list_ticket(msg):
    return handler_check_text_header(msg, ['票务', 'attentez'])

def bl_check_send_message(msg):
    return handler_check_text_header(msg, ['说', 'parlez'])

def bl_response_book(msg):
    return get_reply_text_xml(msg, u'抢票！！')

def bl_response_info_trivial(msg):
    return get_reply_text_xml(msg, u'这里可以打开团委资讯')

def bl_response_info_nearby(msg):
    return get_reply_text_xml(msg, u'这里可以打开近期发票活动')

def bl_response_info_art(msg):
    return get_reply_text_xml(msg, u'这里可以打开近期文艺演出')

def bl_response_list_ticket(msg):
    return get_reply_text_xml(msg, u'这列出所有抢到的票务信息')

def bl_response_send_message(msg):
    return get_reply_text_xml(msg, u'反馈入口')
