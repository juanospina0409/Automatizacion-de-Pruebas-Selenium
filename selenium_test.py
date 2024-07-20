# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Firefox(executable_path=r"C:\Users\juano\Desktop\PROYECTOS VS CODE\CURSOS\Selenium\geckodriver-v0.34.0-win64\geckodriver.exe")
# driver.get("https://www.python.org/")
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait #wait until the elements appear
import time
driver = webdriver.Firefox(executable_path=r"C:\Users\juano\Desktop\PROYECTOS VS CODE\CURSOS\Selenium\geckodriver-v0.34.0-win64\geckodriver.exe")
# driver = webdriver.Edge(executable_path=r"C:\Users\juano\Desktop\PROYECTOS VS CODE\CURSOS\Selenium\edgedriver_win64\msedgedriver.exe")
driver.get("https://gmail.com")

user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
user.send_keys("ohdude040904@hotmail.com")
user.send_keys(Keys.ENTER)

# user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
# user.send_keys("ohdude040904@hotmail.com")
# user.send_keys(Keys.ENTER)



# usuario = driver.find_element(By.ID, "identifierId")
# usuario = send_Keys("ohdude040904@gmail.com")

# password = driver.find_element(By.ID, "")