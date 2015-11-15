import unittest
from selenium import webdriver
 
class IShipSafeTest(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    def test_title(self):
        self.driver.get('http://ishipsafe.com')
        self.assertEqual(
            self.driver.title,
            'iShipSafe')

    def test_homebutton(self):
        self.driver.get('http://ishipsafe.com')
        elem = self.driver.find_element_by_id("logo-container")
        print("home text: " + elem.text);
        self.assertEqual(
            elem.text,
            'iShipSafe')
 
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
