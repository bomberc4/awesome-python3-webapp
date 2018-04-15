'''
Created on 2018年4月15日

@author: bomber
'''
from orm.Field import Field


class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=0, ddl='real'):
        super().__init__(name, ddl, primary_key, default)
