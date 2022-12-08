from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from time import sleep
driver = webdriver.Chrome(executable_path='./utils/chromedriver') # executable_path: chromedriver path

driver.get(url = 'https://gw.dohwa.co.kr/ekp/view/login/userLogin#')
driver.maximize_window()

(
    driver.find_element(
        By.XPATH, 
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/fieldset/div[1]/dl[3]/dd[1]/span/input'
        ).send_keys('221009')
)

(
    driver.find_element(
        By.XPATH, 
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/fieldset/div[1]/dl[3]/dd[2]/div/input'
        ).send_keys('rjskr03#')
)

(
    driver.find_element(
        By.XPATH, 
        '/html/body/div[1]/div/div[2]/div[2]/div[2]/fieldset/div[1]/div/button'
        ).click()
)

da = Alert(driver)
da.accept()

(
    WebDriverWait(driver, 10)
    .until(EC.element_to_be_clickable
    ((
        By.XPATH
        ,'/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/ul/li[7]/a'))
        )
        )

(
    driver.find_element(
        By.XPATH, 
        '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/ul/li[7]/a'
        ).click()
)

