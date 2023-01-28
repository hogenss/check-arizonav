# by HogenSS
# vk.com/sergey_hogen
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import re

#Установка настроек
options = uc.ChromeOptions() 
options.headless=False
options.add_argument('--headless') # Скрытие браузера (имеются с этим проблемы)

# Консоль
print('Укажите никнейм')
print('Важно: Указывайте никнейм такой же, какой он есть на форуме.')
nickname = input() # Ввод никнейма
driver = uc.Chrome(options=options) #Вывод хрома
print('Идёт подсчёт жалоб...')

# Переменные
page = 1
val = 0

# Бесконечный цикл
while True:
    try:
        # Открытие браузера + поиск объекта
        driver.get("https://forum.arizona-v.com/forums/129/page-"+ str(page) + "?last_days=7")
        element = driver.find_elements(By.CLASS_NAME, "structItem")
        sa = driver.find_elements(By.CLASS_NAME, "pageNav-jump--next")

        # Цикл обработки информации
        for e in element:
            res = re.findall(r'Закреплено', e.text) # Проверка закреплена ли жалоба
            resu = re.findall(r'Закрыта', e.text) # Проверка открыта ли жалоба
            if res == []:
                if resu != []:
                    s = re.finditer(r"Просмотры\s(.*)()(мин. назад|[0-9]{1,4})\s([A-z _]{1,30})", e.text, flags=re.S) # Поиск никнейма кто закрыл жалобу
                    for nick in s:
                        d = nick.group(4)
                        if d == nickname: # Если введённый никнейм совпадает с форумом
                            val += 1 # Прибавляем к значению жалоб

        # Автоматическое перелистывание страниц
        if(sa != []): 
            page += 1
        else:
            break
    # error
    except Exception as ex:
        print(ex)

# Вывод после выполнения кода
print('Количество жалоб - ' + str(val))
print('Для закрытия приложения нажмите: Ctrl + C')
input()
