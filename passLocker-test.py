import unittest
from user import User

class TestPassLocker(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Weps', 'pass123') #create user object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username, 'Weps')
        self.assertEqual(self.new_user.password,'pass123')

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple user
        objects to the user_list
        '''
        self.new_user.save_user()
        test_user = User('Test', 'test123')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

if __name__ == '__main__':
    unittest.main()
