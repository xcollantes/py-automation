# Xavier Collantes
# 09/02/18
# Examples tried out from Al Sweigart's book, "Automating the Boring Stuff with Python"
# Web Scraping: Chapter 11

from selenium import webdriver

b = webdriver.Chrome()

type(b)

link = 'https://inventwithpython.com'
b.get(link)