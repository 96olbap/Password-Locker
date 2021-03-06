import unittest
from user import User

class TestUser(unittest.TestCase):
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

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User('Test', 'test123') 
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User('Test', 'test123')
        test_user.save_user()

        user_exists = User.user_exist('Test')
        self.assertTrue(user_exists)


    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User('Test', 'test123')
        test_user.save_user()

        found_user = User.find_by_username("Test")

        self.assertEqual(found_user.password,test_user.password)



    

if __name__ == '__main__':
    unittest.main()
