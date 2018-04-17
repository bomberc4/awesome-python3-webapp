'''
Created on 2018年4月15日

@author: bomber
'''

from orm.Model import Model
from models import next_id
import time
from orm.Field.StringField import StringField
from orm.Field.BooleanField import BooleanField
from orm.Field.FloatField import FloatField


class User(Model):
    __table__ = 'users'
    
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time())
