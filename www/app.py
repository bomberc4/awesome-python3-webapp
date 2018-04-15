'''
Created on 2018年4月15日

@author: bomber
'''
import logging;logging.basicConfig(level=logging.INFO)
from webframe import get
from models.User import User


@get('/')
def index(request):
    users = yield from User.findAll()
    return {
        '__template__':'test.html',
        'users':users
    }
