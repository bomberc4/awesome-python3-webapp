'''
Created on 2018年4月15日

@author: bomber
'''
from orm.Field import Field


class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)
