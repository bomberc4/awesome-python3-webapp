'''
Created on 2018年4月15日

@author: bomber
'''


class APIError(Exception):

    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

        
class APIValueError(APIError):

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)

        
class APIResourceNotFoundError(APIError):

    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfount', field, message)

        
class APIPermissionError(APIError):

    def __init__(self, field, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)
