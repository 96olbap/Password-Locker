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

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username, 'Weps')
        self.assertEqual(self.new_user.password,'pass123')

if __name__ == '__main__':
    unittest.main()
