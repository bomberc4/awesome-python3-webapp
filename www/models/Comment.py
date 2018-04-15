'''
Created on 2018年4月15日

@author: bomber
'''
from orm.Model import Model
from orm.Field.StringField import StringField
from models import next_id
from orm.Field.TextField import TextField
from orm.Field.FloatField import FloatField
import time


class Comment(Model):
    __table__ = 'comments'
    
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)
