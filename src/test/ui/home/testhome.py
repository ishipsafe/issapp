#--------------------------------------------------------#
# IshipSafe Home page UI test cases

# Author: Prasanna Pannuluri
# Date: Dec 03 2015
#--------------------------------------------------------#

import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
 
 
class IShipSafeTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Remote(
            desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
            command_executor='http://24.23.198.139:4444/wd/hub'
            )
        
        
    @classmethod
    def tearDownClass(self):
        self.driver.close()
    
    def test_title(self):
        self.driver.get('http://ishipsafe.com')
        self.assertEqual(
            'Home - iShipSafe',
            self.driver.title)
            
    def test_iShipSafe(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_id("logo-container")
            self.assertEqual('iShipSafe', elem.text)
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_Home(self):
        self.driver.get('http://ishipsafe.com')
        elem    = self.driver.find_element_by_xpath("//a[@href='#']")
        self.assertEqual('Home', elem.text)

    def test_Destinations(self):
        self.driver.get('http://ishipsafe.com')
        elem = self.driver.find_element_by_xpath("//a[@href='#work']")
        self.assertEqual('Destinations', elem.text)

    def test_Contact(self):
        self.driver.get('http://ishipsafe.com')
        elem = self.driver.find_element_by_xpath("//a[@href='#contact']")
        self.assertEqual('Contact', elem.text)

    def test_sender(self):
        self.driver.get('http://ishipsafe.com')
        elem = self.driver.find_element_by_css_selector("#logo-container[href='#Sender']")
        self.assertEqual('SENDER', elem.text)

    def test_flyer(self):
        self.driver.get('http://ishipsafe.com')
        elem = self.driver.find_element_by_css_selector("#logo-container[href='#Flyer']")
        self.assertEqual('FLYER', elem.text)

    def test_sender_overlay(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem1 = self.driver.find_element_by_css_selector("#logo-container[href='#Sender']")
            elem1.click()
            time.sleep(2)
            elem2 = self.driver.find_element_by_id("Sender")
            style = elem2.get_attribute('style')
            self.assertEqual("display: block; top: 10%; opacity: 1;", style, "overlay is not shown")
                  
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_flyer_overlay(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem1 = self.driver.find_element_by_css_selector("#logo-container[href='#Flyer']")
            elem1.click()
            time.sleep(2)
            elem2 = self.driver.find_element_by_id("Flyer")
            style = elem2.get_attribute('style')
            self.assertEqual("display: block; top: 10%; opacity: 1;", style, "overlay is not shown")
                  
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_sender_overlay_header(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#Sender div h4")
            self.assertEqual("Sender", elem.get_attribute('innerHTML'))
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_sender_overlay_paragraph(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#Sender div p")
            t = elem.get_attribute('innerHTML')
            self.assertEqual("We are the amazon of shipping.\nSuper-low prices!!\n60 % cheaper than FedEx, DHL. Even lower than Garudavega!!!!\nThree easy steps:",t)
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_sender_overlay_orderlist1(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#Sender div ol li:nth-child(1)")
            t = elem.get_attribute('innerHTML')
            self.assertEqual("Send email to iShipSafe@gmail.com. Where and what do you want to send to India?", elem.get_attribute('innerHTML'))
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_sender_overlay_orderlist2(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#Sender div ol li:nth-child(2)")
            t = elem.get_attribute('innerHTML')
            self.assertEqual("Know our super-low price estimates. We will pick up your items from your door.", elem.get_attribute('innerHTML'))
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_sender_overlay_orderlist3(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#Sender div ol li:nth-child(3)")
            t = elem.get_attribute('innerHTML')
            self.assertEqual("Delivery and Safety Guaranteed.", elem.get_attribute('innerHTML'))
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_flyer_overlay_header(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#Flyer div h4")
            self.assertEqual("Flyer", elem.get_attribute('innerHTML'))
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_flyer_overlay_paragraph(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#Flyer div p")
            t = elem.get_attribute('innerHTML')
            self.assertEqual("Take our stuff. Earn as much as 150 dollars per bag to India...Wooooow!!\nThree easy steps:", elem.get_attribute('innerHTML'))
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_flyer_overlay_orderlist1(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#Flyer div ol li:nth-child(1)")
            t = elem.get_attribute('innerHTML')
            self.assertEqual("Send email to iShipSafe@gmail.com. Where and when are you flying to India from bay area?", elem.get_attribute('innerHTML'))
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_flyer_overlay_orderlist2(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#Flyer div ol li:nth-child(2)")
            t = elem.get_attribute('innerHTml')
            self.assertEqual("Know your reward amount. We will drop off items at your door step in bay area.", elem.get_attribute('innerHTML'))
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_flyer_overlay_orderlist3(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#Flyer div ol li:nth-child(3)")
            t = elem.get_attribute('innerHTML')
            self.assertEqual("Take these items to India. We will pay you your reward amount that we promised.", elem.get_attribute('innerHTML'))
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_adoption_program_line(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("div.col-md-12.col-md-pull-0-5")
            t = elem.get_attribute('innerHTML')
            self.assertEqual("Be part of our early adopter program",t)

        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_email_logo(self):
        self.driver.get('http://ishipsafe.com')
        try:
            self.driver.find_element_by_css_selector("i.mdi-communication-email")

        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_email_default_text(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("label.blue-text")
            self.assertEqual("Email-id", elem.text)

        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_email_user_entered_text(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#icon_email")
            elem.send_keys("hello@IshipSafe")
            self.assertEqual("hello@IshipSafe", elem.get_attribute('value'))
            
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_join_beta_button_exist(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("button.btn")
            self.assertEqual("JOIN BETA", elem.text)
                
        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_sender_checkbox(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("label[for='sender']")
            self.assertEqual("Sender", elem.text)

        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_flyer_checkbox(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("label[for='flyer']")
            self.assertEqual("Flyer", elem.text)

        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_background_image(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#index-banner")

        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_email_functionality_test1(self):
        self.driver.get('http://ishipsafe.com')
        try:
            button = self.driver.find_element_by_css_selector("button.btn")
            button.click()
            elem_msg = self.driver.find_element_by_css_selector("div.col-md-12.h6")
            time.sleep(2)
            self.assertEqual("Oops something went wrong. Please try again after sometime.", elem_msg.text)

        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    def test_email_functionality_test2(self):
        self.driver.get('http://ishipsafe.com')
        try:
            elem = self.driver.find_element_by_css_selector("#icon_email")
            elem.send_keys("hello@IshipSafe")
            button = self.driver.find_element_by_css_selector("button.btn")               
            button.click()
            elem_msg = self.driver.find_element_by_css_selector("div.col-md-12.h6")
            time.sleep(2)
            self.assertEqual("User already subscribed.", elem_msg.text)

        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    '''
    def test_email_tooltip1(self):
        self.driver.get('http://ishipsafe.com')
        try:
            email = self.driver.find_element_by_css_selector("#icon_email")
            email.send_keys("hello")
            tooltip = self.driver.find_element_by_css_selector("#window-resizer-tooltip")
            print(tooltip.text)

        except NoSuchElementException:
            self.assertTrue(False, "element not found")

    '''
                          
if __name__ == '__main__':
    unittest.main()
