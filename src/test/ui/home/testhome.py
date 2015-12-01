import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
 
class IShipSafeTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()

                 
    @classmethod
    def tearDownClass(self):
        self.driver.close()
    
    def test_title(self):
        self.driver.get('http://ishipsafe.com')
        self.assertEqual(
            self.driver.title,
            'Home - iShipSafe')
            
    def test_iShipSafe(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_id("logo-container")
            print("first text: " + elem.text);
            self.assertEqual(elem.text,'iShipSafe')
        except NoSuchElementException:
            print("*** element not found** ")
            self.assertTrue(False, "element not found")

    def test_Home(self):
        self.driver.get('http://ishipsafe.com')
        elem    = self.driver.find_element_by_xpath("//a[@href='#']")
        print("second text:" + elem.text);
        self.assertEqual(elem.text,'Home')

    def test_Destinations(self):
        self.driver.get('http://ishipsafe.com')
        elem = self.driver.find_element_by_xpath("//a[@href='#work']")
        print("Third text: " + elem.text);
        self.assertEqual(elem.text,'Destinations')

    def test_Contact(self):
        self.driver.get('http://ishipsafe.com')
        elem = self.driver.find_element_by_xpath("//a[@href='#contact']")
        print("fourth text: " + elem.text);
        self.assertEqual(elem.text,'Contact')

    def test_sender(self):
        self.driver.get('http://ishipsafe.com')
        elem = self.driver.find_element_by_css_selector("#logo-container[href='#Sender']")
        print("text1: " + elem.text)
        self.assertEqual(elem.text,'SENDER')

    def test_flyer(self):
        self.driver.get('http://ishipsafe.com')
        elem = self.driver.find_element_by_css_selector("#logo-container[href='#Flyer']")
        print("text2: " + elem.text);
        self.assertEqual(elem.text,'FLYER')

    def test_sender_overlay(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem1 = self.driver.find_element_by_css_selector("#logo-container[href='#Sender']")
            elem1.click()
            time.sleep(2)
            elem2 = self.driver.find_element_by_id("Sender")
            style = elem2.get_attribute('style')
            print(style)
            self.assertEqual("display: block; top: 10%; opacity: 1;", style, "overlay is not shown")
                  
        except NoSuchElementException:
            print("*** element not found** ")
            self.assertTrue(False, "element not found")
                            
   

    

if __name__ == '__main__':
    unittest.main()
