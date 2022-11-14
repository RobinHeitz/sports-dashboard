from unittest import TestCase
import time

from pyvirtualdisplay import Display
from xvfbwrapper import Xvfb

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from handball import handball as hb

from handball.definitions_hb import HandballStanding

class TestVirtualDisplay(TestCase):

    def setUp(self) -> None:
        
        self.display = Display(visible=False, size=(1024,768))
        self.display.start()

        chromeOptions = Options()
        chromeOptions.headless = True

        self.browser = webdriver.Chrome(options=chromeOptions)
    
    def tearDown(self) -> None:
        self.browser.quit()
        self.display.stop()


    def test_ubuntu_homepage(self):
        self.browser.get('http://www.ubuntu.com')
        self.assertIn('Ubuntu', self.browser.title)

    def test_google_homepage(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)



class TestPagesWithXvfbWrapper(TestCase):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.headless = True
        # browser = webdriver.Chrome(executable_path="./drivers/chromedriver", options=chromeOptions)
        

        self.xvfb = Xvfb(width=1280, height=720)
        self.addCleanup(self.xvfb.stop)
        self.xvfb.start()
        self.browser = webdriver.Chrome(options=chromeOptions)
        self.addCleanup(self.browser.quit)

    def testUbuntuHomepage(self):
        self.browser.get('http://www.ubuntu.com')
        self.assertIn('Ubuntu', self.browser.title)

    def testGoogleHomepage(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)



class TestHandballStandings(TestCase):

    def setUp(self) -> None:
        self.url = "https://www.liquimoly-hbl.de/de/liqui-moly-hbl/tabelle/saisonen/tabelle/saison-22-23/gesamt-tabelle/"
        self.xpath = '//*[@id="standings2028776"]/div/table/tbody'

    def test_get_html_code_from_website(self) -> None:
        html_code = hb._get_html_from_website(self.url, self.xpath)
        self.assertTrue(len(html_code)> 50)

    def test_get_bl_standing(self):
        standing:HandballStanding = hb.get_bl_standing(self.url, self.xpath)

        self.assertIsNotNone(standing)
        self.assertTrue(type(standing), HandballStanding)
        self.assertIsNotNone(standing.table)