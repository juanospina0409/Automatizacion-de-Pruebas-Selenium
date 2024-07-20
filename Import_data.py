from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait #wait until the elements appear
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Firefox WebDriver with the path to geckodriver
driver = webdriver.Firefox(executable_path=r"C:\Users\juano\Desktop\PROYECTOS VS CODE\CURSOS\Selenium\geckodriver-v0.34.0-win64\geckodriver.exe")
# driver = webdriver.Edge(executable_path=r"C:\Users\juano\Desktop\PROYECTOS VS CODE\CURSOS\Selenium\edgedriver_win64\msedgedriver.exe")
# driver.get("https://login.live.com") #this is for OUTLOOK
driver.get("https://accounts.google.com/ServiceLogin") #this is for GMAIL


try:
    # Wait until the email input field is present and send the email
    user = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.NAME, "loginfmt"))
        EC.presence_of_element_located((By.ID, "identifierId")) #i0116
    )
    user.send_keys("ohdude040904@hotmail.com")
    user.send_keys(Keys.ENTER)
    
    # Wait until the password input field is present and send the password
    password = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.NAME, "passwd"))
        EC.presence_of_element_located((By.ID, "i0118"))
    )
    password.send_keys("Cuentafake.1357")
    password.send_keys(Keys.ENTER)
    
    # Add a delay to observe the result (optional)
    time.sleep(5)

finally:
    # Close the browser
    driver.quit(driver, 30)
