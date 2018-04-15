'''
Created on 2018年4月15日

@author: bomber
'''
import time
import uuid


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4(), hex)
