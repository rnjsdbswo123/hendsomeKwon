from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert #팝업해결
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




delivery = list(set([

    # 주소 입력

]))
count = 0

driver = webdriver.Chrome()
# 로그인
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
sleep(0.5)

driver.execute_script("document.getElementById('id').value = '아이디 입력'")  # 아이디 입력
sleep(0.5)
driver.execute_script("document.getElementById('pw').value = '비밀번호입력'") #비밀번호 입력
sleep(0.5)
driver.find_element_by_xpath('//*[@id="log.login"]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[5]/a').click()
sleep(1)



for i in delivery:
    try:
        wait = WebDriverWait(driver, 2)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.input_search")))
        sleep(2)
        element.send_keys("제주 " + i + "(1)")
        sleep(2)
        element.send_keys(Keys.ENTER)
        sleep(2)
        driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-address/div/div[2]/div/div[1]/div[2]/div[2]/button[1]').click()
        sleep(2)
        element.send_keys(Keys.ENTER)
        sleep(2)
        element.send_keys(Keys.ENTER)
        driver.get('https://map.naver.com/v5/')
        count += 1
        print("총 " + str(len(delivery)) + "개 중 " + str(count) + "개 완료.")
    except Exception:
        print(i + "실패!!!!")
        driver.get('https://map.naver.com/v5/')

