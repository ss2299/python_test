from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
import pandas as pd
import time

# Web Browser 드라이버 실행
# MAC OS
browser = webdriver.Firefox(executable_path="/usr/local/Cellar/geckodriver/0.30.0/bin/geckodriver")
browser.get("http://www.naver.com")

# page = 'http://www.naver.com'
# driver.get(page)