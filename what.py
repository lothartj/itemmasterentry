import tkinter as tk
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import re
import datetime
import os
import sys
import pyautogui as py
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import pyautogui


PATH = ('C:/msedgedriver.exe')
driver = webdriver.Edge(PATH)
driver.get(
    'https://')


time.sleep(2)

py.hotkey('tab')
py.typewrite(input(''))
py.hotkey('tab')
py.typewrite(input(''))
py.hotkey('enter')

time.sleep(10)

# Click search
# wait for the element to be visible, to click new
click_search = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/button[3]'))
)

# click the element
click_search.click()
time.sleep(4)
py.typewrite('Items')

# switch to the iframe
iframe = driver.find_element(By.CSS_SELECTOR, 'iframe.designer-client-frame')
driver.switch_to.frame(iframe)


# Click Items
# wait for the element to be visible, to click new
click_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/form/main/div/div[3]/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[1]'))
)

# # click the element
click_items.click()

# Click Items search
# wait for the element to be visible, to click new
click_items_search = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div/div[3]/form/main/div[2]/div[4]/div/div/div/div[1]/div[2]/div/div[2]/div[1]'))
)

# # click the element
click_items_search.click()

time.sleep(4)
py.typewrite('Z-')

time.sleep(10)


# Change the layout
layout = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/form/main/div[2]/div[4]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/button'))
)
layout.click()

time.sleep(2)

# Click List
list = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/form/main/div[2]/div[7]/div/div/div/div[3]/div/div/ul/li[1]/div/button'))
)
list.click()

time.sleep(2)

# create an empty list to store the anchor text objects
z_codes = []
n_codes = []
z_code_attributes = False

# Find the table element
table_element = driver.find_element(
    By.XPATH, "/html/body/div[1]/div[3]/form/main/div[2]/div[6]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/table")

# Find the tbody element
table_body = table_element.find_element(
    By.TAG_NAME, "tbody")

tr_index_code = 1
code_index = 0


# Loop throught the Item z- index and grab all Item No.

for table_row in table_body.find_elements(
        By.TAG_NAME, "tr"):
    table_data = table_row.find_element(
        By.XPATH, f"/html/body/div[1]/div[3]/form/main/div[2]/div[6]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[{ tr_index_code }]/td[3]")
    table_code = table_data.find_elements(By.TAG_NAME, "a")

    table_code_elements = table_data.find_elements(By.TAG_NAME, "a")
    if len(table_code_elements) > 0:
        table_code = table_code_elements[0]
        z_codes.append({'code': table_code.text, 'Attr': []})

    else:
        print("No <a> element found in table cell")
    tr_index_code = tr_index_code + 1
    # print(table_code.text)


# Changing the z-codes to normal codes
for item in z_codes:
    code = item['code']
    code = code.replace("Z-", "")
    n_codes.append({'n_code': code})


print(z_codes)
print(n_codes)


# Grab all the attribues from the n_codes, do this if z_codes is greater then 0

while len(n_codes) > 0:

    for normal_codes in n_codes:
        # Click the search button
        searchBTN = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[3]/form/main/div[2]/div[4]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/input'))
        )
        searchBTN.click()
        py.hotkey('backspace')
        py.hotkey('backspace')
        py.typewrite(normal_codes['n_code'])

        # Click the item No
        clickNormalItem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[3]/form/main/div[2]/div[6]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[3]'))
        )
        clickNormalItem.click()

        # Click the item bar
        itemBTN = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[5]/form/main/div[2]/div[4]/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/button'))
        )
        itemBTN.click()

        # Click the Attributes
        attributesBTN = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[5]/form/main/div[2]/div[4]/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/button'))
        )
        attributesBTN.click()

time.sleep(5)
