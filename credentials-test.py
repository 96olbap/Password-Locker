import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours
    '''
    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        self.new_cred = Credentials('twitter', 'manzzalvin', 'pass123')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_cred.acc_name, 'twitter')
        self.assertEqual(self.new_cred.acc_username,'manzzalvin')
        self.assertEqual(self.new_cred.acc_password, 'pass123')

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
        the credentials_list
        '''
        self.new_cred.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to the credentials_list
        '''
        self.new_cred.save_credentials()
        test_cred = Credentials('twitter', 'manzzalvin', 'pass123')
        test_cred.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credentials object from our credentials_list
        '''
        self.new_cred.save_credentials()
        test_cred = Credentials('twitter', 'manzzalvin', 'pass123') 
        test_cred.save_credentials()
        self.new_cred.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''
        self.new_cred.save_credentials()
        test_cred = Credentials('twitter', 'manzzalvin', 'pass123')
        test_cred.save_credentials()

        cred_exists = Credentials.credentials_exist('manzzalvin')
        self.assertTrue(cred_exists)

    def test_display_all_cred(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.new_cred.save_credentials()
        allCredentials_list = [Credentials.display_credentials()]
        self.assertEqual(allCredentials_list, Credentials.credentials_list)
        # self.assertEqual(Credentials.display_credentials().acc_username, Credentials.credentials_list[0].acc_username)

    def test_find_cred_by_username(self):
        '''
        test to check if we can find a user's credentials by username and display information
        '''

        self.new_cred.save_credentials()
        test_cred = Credentials('twitter', 'manzzalvin', 'pass123')
        test_cred.save_credentials()

        found_cred = Credentials.find_by_acc_username("manzzalvin")

        self.assertEqual(found_cred.acc_password, test_cred.acc_password)

if __name__ == '__main__':
    unittest.main()
