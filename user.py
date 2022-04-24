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

    def save_user(self):
        '''
        save_user method saves a user object into the user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        display_users method shows saved users from the user_list
        '''
        return cls.user_list

    @classmethod
    def user_exist(cls,number):
        '''
        user_exists method checks if a user exists from the user_list
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == number:
                return True
                return False
