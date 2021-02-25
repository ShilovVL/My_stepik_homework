from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element(
    (By.ID, "price"), "$100"))
       
    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)

    y = calc(x)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)


    button = browser.find_element_by_css_selector('[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')


finally:
    time.sleep(15)

    # закрываем браузер после всех манипуляций
    browser.quit()
