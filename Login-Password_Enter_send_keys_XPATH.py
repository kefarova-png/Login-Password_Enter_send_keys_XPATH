#  Импортируем необходимые библиотеки и модули
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#  Chrome. Создаём переменную для опций браузера
options = webdriver.ChromeOptions()
#  Пишем в опции: detach, True -- чтобы Chrome не закрывал окно браузера после завершения работы кода
options.add_experimental_option("detach",True)
#  Создаём вебдрайвер Chrome, с автоматической проверкой/установкой драйвера и c настройками, которые в options
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)
#  Открываем вебдрайвером ссылку
driver.get('https://app.imyx.ru/auth?redirect=/&utm_source=yandex&utm_medium=cpc&utm_campaign=ya_adult_maxcash&utm_content=1907242160146401260&utm_term=---autotargeting')
#  Устанавливаем размер окна
driver.set_window_size(1920,1080)

#  Находим элемент для логина, используя XPATH
user_name = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[1]/input")
user_name.send_keys("not_office@mail.ru")  #  Вводим в поле "not_office@mail.ru"

#  Находим элемент для пароля, используя XPATH
user_password = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[2]/div/input")
user_password.send_keys("Shur_1234")  #  Вводим в поле "Shur_1234"

#  Найдём и нажмём кнопку входа
button_for_login = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/button")
button_for_login.click()

# Пауза для визуальной проверки
time.sleep(10)
# Закрываем браузер
driver.close()