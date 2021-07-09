from selenium import webdriver
from fake_useragent import UserAgent

useragent = UserAgent()
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent.random)
firefox_driver = webdriver.Firefox(firefox_profile=profile)


url = "https://www.google.com"
firefox_driver.get(url)