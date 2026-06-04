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

#  Находим элемент для логина, используя XPATH, и Вводим в поле логина "to del using clear"
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys("to del using clear")
print('Login input')

#  Находим элемент для пароля, используя XPATH, и Вводим в поле пароль "to delete using Ctrl+'a' & DELETE"
user_password = driver.find_element(By.XPATH, "//input[@id='password']")
user_password.send_keys("to delete using Ctrl+'a' & DELETE")
print('Password input')
time.sleep(3)  #  Для визуального контроля за происходящим

#  Очистим содержимое поля логина
user_name.clear()
print('Login cleared')
time.sleep(2)  #  Для визуального контроля за происходящим

#  Вводим в поле логин "standard_user"
user_name.send_keys("standard_user")
print('Login input')
time.sleep(2)  #  Для визуального контроля за происходящим

#  Выделим содержимое поля пароля и удалим его
user_password.send_keys(Keys.CONTROL + 'a')
print('Password selected')
time.sleep(2)  #  Для визуального контроля за происходящим
user_password.send_keys(Keys.DELETE)
print('Password removed')
time.sleep(2)  #  Для визуального контроля за происходящим

#  Вводим в поле пароля "secret_sauce"
user_password.send_keys("secret_sauce")
print('Password input')
time.sleep(2)  #  Для визуального контроля за происходящим

#  Жмём кнопку авторизации
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(2)  #  Для визуального контроля за происходящим

#  Закрываем браузер
driver.close()