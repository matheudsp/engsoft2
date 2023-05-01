from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

# Define Brave path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = webdriver.ChromeOptions()
options.binary_location = brave_path

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  
        self.fail('Finish the test!')  

        # She is invited to enter a to-do item straight away
        # [...rest of comments as before]

if __name__ == '__main__':  
    unittest.main()