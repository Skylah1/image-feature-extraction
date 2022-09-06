import time
import os
import random
from unittest import result
import pyperclip
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSessionIdException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

'''
python 3.7

'''

def main() :

    driver = setDriver('./chromedriver.exe', setChromeOpt())

    """
    수집하기
    """
    
    # 사이트 url
    site_url = 'https://m19.kotbc.com/'
    """
    *특이사항
      - 애니 카테고리는 다른 사이트로 이동
    """
    
    # 카테고리 셀렉터
    cate_selector = 'div ul.menu-ul li.mmmum a'
    # 타이틀 셀렉터
    title_selector = 'div.list-row div.list-text a'
    # 목차 셀렉터
    index_selector = 'li.list-item a'
    # 이미지 셀렉터
    img_selector = 'div.image img'

    content_selector = 'div.view-cont'

    # 대기시간
    d_time = 5

    # 기록할 txt 파일 오픈 
    f = wLog (None, '--- 크롤링 시작 ---' ,'', enter = 2, flag='open')

    # 해당 사이트로 이동
    getUrl(driver, site_url, d_time)
    
    # 카테고리 (a태그) 요소
    for idx in range(len(getElement(driver, cate_selector))) :

        # 카테고리 클릭
        clickElementIdx(driver, cate_selector, idx)

        # 컨텐츠 제목(a태그) 요소
        # 컨텐츠 제목별
        for title_attr in getElement(driver, title_selector) :
            wLog(f, '제목', getAttr(element = title_attr))

            #새탭열기
            wLog(f, '목차 url ', openNewTab(driver, title_attr, d_time ))

            #컨텐츠 목차 <- n번째 컨텐츠의 1~m까지의 에피소드(목차) 가져오기
            # 1~m번째 에피소드에 차례대로 접근하여 내용 가져오기 
            for index_attr in getElement(driver, index_selector) :

                wLog(f, '컨텐츠 목록 제목 ', getAttr(element=index_attr))
 
                #새창열기
                wLog(f, '컨텐츠 url ', openNewWindow(driver, index_attr, d_time ))
                wLog(f, '포스터 src ', getAttr(selector = [driver, img_selector], attr = 'src'))

                # 홈페이지마다 정보 페이지의 셀랙터 및 표현방식이 다를 것으로 예상
                info = getElement(driver, 'div.list p')
                for c in info :
                    tab = getElement(driver, 'span', parent=c)
                    wLog(f, getAttr(tab[0]), getAttr(tab[1]))

                #content = getElement(driver, 'div.view-cont', list=False)

                wLog(f, '컨텐츠 내용', getAttr(selector = [driver, content_selector]), enter=2)

                # 닫기
                closeCurrentWindow(driver)

            # 닫기
            closeCurrentWindow(driver)
                    
    wLog(f, '----- 채증 완료. -----', '', enter=2, flag='close')





# Chrome Driver Option Setting
def setChromeOpt (headless = True) :

    chrome_options = Options()
    # 창 없이 크롤링
    if headless :
        chrome_options.add_argument("headless")

    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--start-maximized")        
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-blink-features")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")      
    chrome_options.add_argument("force-device-scale-factor=1")
    chrome_options.add_argument("high-dpi-support=1")
    chrome_options.add_argument("loggingPrefs=performance1")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--force-renderer-accessibility")

    #창 크기 조절
    chrome_options.add_argument("window-size=2560,1440")

    return chrome_options

# Driver
def setDriver (driverPath, option) :
    driver = webdriver.Chrome(executable_path = driverPath, desired_capabilities=DesiredCapabilities.CHROME, chrome_options=option)
    return driver


# 엘리먼트 요소 가져오기
def getElement (driver, selector, parent= None, list = True):

    if parent :
        driver = parent
    
    # 셀랙터로 요소 배열 get
    if list :
        element = driver.find_elements(by=By.CSS_SELECTOR, value=selector)
    else :
    # 셀랙터로 첫번째 요소 get
        element = driver.find_element(by=By.CSS_SELECTOR, value=selector)

    return element

# 해당 엘리먼트의 n번째 요소 가져와서 클릭
def clickElementIdx (driver, selector, idx):
    getElement(driver, selector, list=True)[idx].click()


# 해당 요소 속성값 가져오기
def getAttr (element = None , selector = [],  attr='text'):

    # selector를 인자로 받는 경우 추가
    if element is None :
        element = getElement( selector[0], selector[1] , list=False) # driver, selector

    if attr == 'text' :
        result = element.text
    else :
        result = element.get_attribute(attr)
    return result

# 현재 창에서 url로 이동
def getUrl(driver, url, d_time = 10):
    driver.get(url)
    time.sleep(d_time)

# 새탭으로 오픈
def openNewTab (driver, attr, d_time = 10) :
    # get url 
    url = attr.get_attribute('href')

    #새탭열기
    driver.execute_script(f'''
    window.open("{url}","width="+screen.availWidth+",height="+screen.availHeight);            
    ''')
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])
    driver.implicitly_wait(d_time)

    return url

# 새창으로 오픈
def openNewWindow (driver, attr, d_time = 10) :
    # get url 
    url = attr.get_attribute('href')

    #새창열기
    driver.execute_script(f'''
    window.open("{url}","PopupWin","width="+screen.availWidth+",height="+screen.availHeight);            
    ''')
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])
    driver.implicitly_wait(d_time)

    return url

# 마지막으로 연 창을 닫음
def closeCurrentWindow (driver) :
    driver.close()
    window_handlers = driver.window_handles
    driver.switch_to.window(window_handlers[-1])

# print, txt 기록
def wLog (file, message='' ,txt='', enter = 1, flag = None):
    
    if flag == 'open' :
        file = open('data/log.txt', 'a')

    newline = '\n'*enter
    print(f"[{time.time()}]{message} : {txt} {newline}", end='')
    file.write(f"{message} : {txt} {newline}")

    if flag == 'close' :
        file.close()

    return file


if __name__ == '__main__':

    main()