# Required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Define Brave path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = webdriver.ChromeOptions()
options.binary_location = brave_path


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('http://127.0.0.1:8000/')

# assert 'Django' in driver.title


