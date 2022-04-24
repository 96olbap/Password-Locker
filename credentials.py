class Credentials:
    '''
    Class that generates instances of credentials
    '''
    credentials_list = []
    def __init__(self, acc_name, acc_username, acc_password):
        '''__init__ method that helps define properties to the class objects
        '''
        self.acc_name = acc_name
        self.acc_username = acc_username
        self.acc_password = acc_password

    def save_credentials(self):
        '''
        save_credentials method saves the users account credentials into the credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes saved credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        display_credentials method shows saved credentials from the credentials_list
        '''
        for credential in cls.credentials_list:
            return cls.credentials_list

    @classmethod
    def credentials_exist(cls,number):
        '''
        credentials_exist method checks if a credentials object exists from the credentials_list
        Returns :
            Boolean: True or false depending if the object exists
        '''
        for credentials in cls.credentials_list:
            if credentials.acc-username == number:
                return True
                return False


    
