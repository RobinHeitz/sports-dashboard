from selenium import webdriver
from selenium.webdriver import chromium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display

# set xvfb display since there is no GUI in docker container.

display = Display(visible=False, size=(1024, 768))
display.start()

chrome_options = Options()
# chrome_options.BinaryLocation = "/usr/bin/chromium-browser"
chrome_options.headless = True

service = Service(executable_path='/usr/local/bin/chromedriver')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")


# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument("--window-size=1920,1200")
# options.headless = True

# driver = webdriver.Chrome(options=chrome_options)

# browser = webdriver.Chrome(options=chrome_options)
# browser.get("https://google.de")


print("init chrome")
