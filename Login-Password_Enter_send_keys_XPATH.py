#  Импортируем необходимые библиотеки и модули
import time
from selenium.webdriver.common.keys import Keys
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
driver.get('https://saucedemo.com/')
#  Устанавливаем размер окна
driver.set_window_size(1920,1080)

#  Находим элемент для логина, используя XPATH, и Вводим в поле логин "standard_user"
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
print('Login input')
time.sleep(2)  #  Для визуального контроля за происходящим

#  Выделим содержиое поля логина и удалим его
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(Keys.CONTROL + 'a')
print('Login selected')
time.sleep(2)  #  Для визуального контроля за происходящим
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(Keys.BACKSPACE)
print('Login removed')

#  Находим элемент для пароля, используя XPATH, и Вводим в поле пароль "secret_sauce_"
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce_")
print('Password input')
time.sleep(2)  #  Для визуального контроля за происходящим

#  Выделим содержиое поля пароля и удалим его
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(Keys.CONTROL + 'a')
print('Password selected')
time.sleep(2)  #  Для визуального контроля за происходящим
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(Keys.DELETE)
print('Password removed')
time.sleep(2)  #  Для визуального контроля за происходящим

#  Нажмём кнопку ENTER на клавиатуре при активном поле ввода пароля
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(Keys.ENTER)
print('ENTER pressed')
time.sleep(2)  #  Для визуального контроля за происходящим

# #  Найдём и нажмём кнопку входа
# driver.find_element(By.XPATH, "//input[@id='login-button']").click()
# print('Login button click')

#  Обновляем страницу
driver.refresh()
print("Page refresh")
time.sleep(2)  #  Для визуального контроля за происходящим

#  Закрываем браузер
driver.close()