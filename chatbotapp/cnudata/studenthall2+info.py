from enum import Enum
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import requests
from bs4 import BeautifulSoup
import datetime
import time

# 현재 날짜 생성
raw_date = datetime.datetime.now()
now = raw_date.strftime('%Y-%m-%d')


# numbering
class Cafeteria(Enum):
    student_hall_1 = "1"
    student_hall_2 = "2"
    student_hall_3 = "3"
    sangrok_student_hall = "4"
    college_of_domestic_science = "5"


# 옵션 생성
options = webdriver.ChromeOptions()
# 대상거부 방지
# headers = 'User -Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
# options.add_argument(headers)
# 창 숨기는 옵션 추가
# options.add_argument("headless")
# driver 실행
# browser = webdriver.Chrome('chromedriver',chrome_options=options)
# choose frame "menu" or "bottom"
browser = webdriver.Chrome(r"C:\Users\woner\Desktop\coding\chatbot_cnu\project\chromedriver.exe",
                           chrome_options=options)


def get_soup(frame):
    url = "http://cnuis.cnu.ac.kr/jsp/etc/weekMenuFrame.jsp"
    browser.get(url)
    element = browser.find_element_by_name(frame)
    browser.switch_to.frame(element)
    soup = BeautifulSoup(browser.page_source, "lxml")
    return soup

    # soup + "_" + frame = BeautifulSoup(browser.page_source, "lxml")
    # return


# 오늘 날짜와 비교하여서 그날짜 값의 index 반환 > 그 index 를 활용해 오늘 날짜메뉴 얻기

def get_date_index():
    browser.switch_to_default_content()
    browser.switch_to_frame("bottom")
    soup_bottom = BeautifulSoup(browser.page_source, "lxml")

    datas = soup_bottom.find_all("td", attrs={"id": "cc1"})
    today = ""
    count = 0
    for idx, data in enumerate(datas, start=3):
        data = data.get_text().strip()
        if (data == now):
            count = idx
            break
    browser.quit()
    return count


# 조식 , 석식 , 석식 , 일품(석식) 일품(석식) 페이지 띄워주기 !
def set_timezone(timezone):
    soup_menu = get_soup("menu")
    select = Select(browser.find_element_by_name("food_div_cd"))
    select.select_by_visible_text(timezone)

    # 조회버튼 클릭
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[8]/input').click()


# 제 1학생회관을 제외화고 menu 가져옴 조식 석식 석식
def number_timezone(idx):
    dict_number_of_timezone = {
        1: '조식',
        2: '중식',
        3: '석식',
        4: '일품(중식)',
        5: '일품(석식)'
    }
    return dict_number_of_timezone.get(idx, '{} is invalid index(1-5)'.format(idx))


def get_recipe(cafeteria):
    cafeteria_info = {"restaurant": cafeteria.name}
    count = 1  # 조식:1 중식:2 석식:3 특중:4 특석:5
    # 석식 크롤링
    for when in ["조식", "중식", "석식", "일품(중식)", "일품(석식)"]:

        set_timezone(when)

        browser.switch_to_default_content()
        browser.switch_to_frame("bottom")
        soup_bottom = BeautifulSoup(browser.page_source, "lxml")
        where = cafeteria.value
        column = int(where) + 1
        # 이때 row는 오늘 날짜에 해당하는tr[여기들어갈숫자]

        datas = soup_bottom.find_all("td", attrs={"id": "cc1"})
        row = 0
        for idx, data in enumerate(datas, start=3):
            data = data.get_text().strip()
            if (data == "2021-02-18"):
                row = idx
                break
        # 메뉴가 존재하면 tbody 가있음!

        try:
            tr_tag = soup_bottom.find_all("td", attrs={"id": "cc1"})[row - 3].parent
            menus = tr_tag.find("tbody").find_all("td")
            for menu in menus:
                print(menu.get_text().strip(), end=",")

        except:
            print("금일 운영을 하지않습니다", end="")
        print()
        count += 1
        print(number_timezone(count))

    browser.quit()


def make_answer_food_menu(user_answer=''):
    cafeterias = {
        "제1학생회관": Cafeteria.student_hall_1,
        "제2학생회관": Cafeteria.student_hall_2,
        "제3학생회관": Cafeteria.student_hall_3,
        "제4학생회관": Cafeteria.sangrok_student_hall,
        "생활과학대학": Cafeteria.college_of_domestic_science
    }

    cafeteria = cafeterias[user_answer]
    get_recipe(cafeteria)


make_answer_food_menu("제2학생회관")











