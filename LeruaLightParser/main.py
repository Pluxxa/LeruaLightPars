from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def main():
    try:

        browser = webdriver.Firefox()
        browser.get("https://leroymerlin.ru/catalogue/osveshchenie/?page=1")

        time.sleep(10)
    finally:
        browser.quit()
        print("Программа завершена.")

if __name__ == "__main__":
    main()