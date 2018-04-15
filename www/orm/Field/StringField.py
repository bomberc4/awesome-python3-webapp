'''
Created on 2018年4月15日

@author: bomber
'''
from orm.Field import Field


class StringField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100'):
        super().__init__(name, ddl, primary_key, default)