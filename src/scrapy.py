from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.google.com"
chrome_driver.get(url)
