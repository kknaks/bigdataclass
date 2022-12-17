from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from time import sleep


driver = webdriver.Chrome(executable_path='./utils/chromedriver') # executable_path: chromedriver path
#그룹웨어 접속
driver.get(url = 'https://gw.dohwa.co.kr/ekp/view/login/userLogin#')
driver.maximize_window()

while True:
    ID = input('사번을 입력하세요 : ')
    #사번입력
    (
        driver.find_element(
            By.XPATH, 
            '/html/body/div[1]/div/div[2]/div[2]/div[2]/fieldset/div[1]/dl[3]/dd[1]/span/input'
            ).send_keys('221009')
    )

    # #비밀번호 입력
    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div[1]/div/div[2]/div[2]/div[2]/fieldset/div[1]/dl[3]/dd[2]/div/input'
    #         ).send_keys('rjskr03#')
    # )

    # #로그인 버튼
    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div[1]/div/div[2]/div[2]/div[2]/fieldset/div[1]/div/button'
    #         ).click()
    # )

    # sleep(1)

    # #팝업창 확인
    # da = Alert(driver)
    # da.accept()

    # #업무방 들어가기
    # (
    #     WebDriverWait(driver, 10)
    #     .until(EC.element_to_be_clickable
    #     ((
    #         By.XPATH
    #         ,'/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/ul/li[7]/a'))
    #         )
    #         )

    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/ul/li[7]/a'
    #         ).click()
    # )

    # sleep(1)

    # #콘도신청 클릭
    # driver.switch_to.frame('subBody')

    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[1]/div[2]/div[3]/ul/li[2]/div/a'
    #         ).click()
    # )

    # sleep(1)

    # #리솜리조트 선택
    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[2]/div[2]/div/select'
    #         ).click()
    # )

    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[2]/div[2]/div/select/option[28]'
    #         ).click()
    # )

    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[3]/div[4]/table/tbody/tr[1]/td[1]/input[1]'
    #         ).click()
    # )

    # (
    #     WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable(
    #             (By.XPATH,
    #             '/html/body/div[2]/div[1]/button' )
    #             )
    #             )
    # )


    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div[2]/div[1]/button'
    #         ).click()
    # )

    # #입실일 선택
    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[3]/div[4]/table/tbody/tr[1]/td[1]/input[1]'
    #         ).click()
    # )

    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div[2]/div[2]/div/table/tbody/tr[5]/td[3]'
    #         ).click()
    # )

    # #퇴실일 선택
    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[3]/div[4]/table/tbody/tr[1]/td[1]/input[2]'
    #         ).click()
    # )

    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div[2]/div[2]/div/table/tbody/tr[5]/td[4]'
    #         ).click()
    # )

    # #이메일 입력
    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[3]/div[4]/table/tbody/tr[1]/td[2]/input'
    #         ).send_keys('khlee.official@dohwa.co.kr')
    # )

    # #휴대폰 번호 입력
    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[3]/div[4]/table/tbody/tr[2]/td[1]/input[1]'
    #         ).send_keys('010')
    # )

    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[3]/div[4]/table/tbody/tr[2]/td[1]/input[2]'
    #         ).send_keys('5511')
    # )

    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[3]/div[4]/table/tbody/tr[2]/td[1]/input[3]'
    #         ).send_keys('3764')
    # )

    # #사내 번호 입력
    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[3]/div[4]/table/tbody/tr[2]/td[2]/input[1]'
    #         ).send_keys('02')
    # )

    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[3]/div[4]/table/tbody/tr[2]/td[2]/input[2]'
    #         ).send_keys('6323')
    # )

    # (
    #     driver.find_element(
    #         By.XPATH, 
    #         '/html/body/div/div/div/div[2]/div[3]/div[4]/table/tbody/tr[2]/td[2]/input[3]'
    #         ).send_keys('3836')
    # )

    # #신청하기
    # # (
    # #     driver.find_element(
    # #         By.XPATH, 
    # #         '/html/body/div/div/div/div[2]/div[3]/p/button'
    # #         ).click()
    # # )
