import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import re
options = uc.ChromeOptions()
#options.headless=True
#options.add_argument('--headless')
print('Укажите никнейм')
print('Важно: Указывайте никнейм такой же, какой он есть на форуме.')
nickname = input()
driver = uc.Chrome(options=options)
page = 1
val = 0

while True:
    try:
        driver.get("https://forum.arizona-v.com/forums/129/page-"+ str(page) + "?last_days=7")
        element = driver.find_elements(By.CLASS_NAME, "structItem")
        sa = driver.find_elements(By.CLASS_NAME, "pageNav-jump--next")
        for e in element:
            res = re.findall(r'Закреплено', e.text)
            resu = re.findall(r'Закрыта', e.text)
            if res == []:
                if resu != []:
                    s = re.finditer(r"Просмотры\s(.*)()(мин. назад|[0-9]{1,4})\s([A-z _]{1,30})", e.text, flags=re.S)
                    for nick in s:
                        d = nick.group(4)
                        if d == nickname:
                            val += 1
                    
            #print(e.text)
        if(sa != []):
            page += 1
        else:
            break
    except Exception as ex:
        print(ex)
print('Количество жалоб - ' + str(val))
input()