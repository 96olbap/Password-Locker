class User:
    '''
    Class that generates new instances of users
    '''
    user_list = []

    def __init__(self, username, password):
        '''
        __init__ method to help define the properties of the user object
        '''
        self.username = username
        self.password = password
        