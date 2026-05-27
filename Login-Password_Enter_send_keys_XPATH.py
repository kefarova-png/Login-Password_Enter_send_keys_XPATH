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
driver.get('https://saucedemo.com/')
#  Устанавливаем размер окна
driver.set_window_size(1920,1080)

#  Находим элемент для логина, используя XPATH, и Вводим в поле логин "standard_user_"
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user_")
print('Incorrect login input')

#  Находим элемент для пароля, используя XPATH, и Вводим в поле пароль "secret_sauce_"
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce_")
print('Incorrect password input')

#  Найдём и нажмём кнопку входа
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
print('Login button click')

#  Паузы для визуальной проверки
time.sleep(3)
driver.refresh()  #  обновляем страницу
print("Page refresh")
time.sleep(2)

#  Закрываем браузер
driver.close()