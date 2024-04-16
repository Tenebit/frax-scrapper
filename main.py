from bs4 import BeautifulSoup
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import undetected_chromedriver as uc 
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from fastapi.responses import JSONResponse

app = FastAPI()
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from seleniumwire import webdriver
import seleniumwire.undetected_chromedriver as uc
from seleniumwire.utils import decode
import json

import time

# Configuración del navegador (Asegúrate de tener el chromedriver correcto para tu versión de Chrome y tu SO)
chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--headless')  # Sin GUI
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(
    options=chrome_options,
    seleniumwire_options={}
)


# Navegar a la página
driver.get('https://www.fraxplus.org/calculation-tool/')
driver.set_window_size(1640, 1900)
wait = WebDriverWait(driver, 20)



driver.save_screenshot('inicial.png')
# Información del paciente
driver.find_element(By.NAME, 'inputIdentificationText').send_keys('Camilo Duque')
driver.find_element(By.NAME, 'inputAgeText').send_keys('19830908') #se debe ingresar fecha de nacimiento sin guiones aaaammdd

# Información de Continente
driver.find_element(By.XPATH,"//div[@id='calculationToolContainer']/div/div/div/div/div[2]/div/div/div/div[2]").click()
driver.implicitly_wait(1)
driver.find_element(By.XPATH,"//div[@id='react-select-2-option-2']/div").click()

# Información de País
driver.find_element(By.XPATH,"//div[@id='calculationToolContainer']/div/div/div[2]/div/div[2]/div/div/div/div[2]").click()
driver.implicitly_wait(1)
driver.find_element(By.XPATH,"//div[@id='react-select-3-option-3']/div/span").click()

# Información de Peso y Estatura
driver.find_element(By.NAME, 'inputWeightText').send_keys('83')
driver.find_element(By.NAME, 'inputHeightText').send_keys('181')

#Genero
driver.find_element(By.ID, 'M').click()

# 5. Previous Fracture
driver.find_element(By.XPATH,"//label[@id='advanced-checkbox']/span").click()

# 6. Parent Fractured Hip
driver.find_element(By.XPATH,"(//label[@id='advanced-checkbox']/span)[2]").click()

# 7. Current Smoking
driver.find_element(By.XPATH,"(//label[@id='advanced-checkbox']/span)[3]").click()

# 8. Glucocorticoids
driver.find_element(By.XPATH,"(//label[@id='advanced-checkbox']/span)[4]").click()

# 9. Previous Fracture
driver.find_element(By.XPATH,"(//label[@id='advanced-checkbox']/span)[5]").click()

# 10. Secondary osteoporosis
driver.find_element(By.XPATH,"(//label[@id='advanced-checkbox']/span)[6]").click()

# 11. Secondary osteoporosis
driver.find_element(By.XPATH,"(//label[@id='advanced-checkbox']/span)[7]").click()

#12 . Femoral neck BMD
# driver.find_element(By.XPATH,"//div[@id='calculationToolContainer']/div[3]/ol/div/div[2]/div/div[2]/div/div/div/div/div[2]").click()
# driver.implicitly_wait(1)
# driver.find_element(By.XPATH,"//div[@id='react-select-5-listbox']/div/div").click()

# Enviar formulario dando click en el botón Calculate
driver.find_element(By.CLASS_NAME, "btn-primary").click()

# Iniciamos la espera del request, esto se hace con la libreria selenium-wire que permite interceptar los request
request = driver.wait_for_request('https://calculator.fraxplus.org/fraxScore')
response_text = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
string_data = response_text.decode('utf-8')  # Decoding bytes to string
json_data = json.loads(string_data)  # Parsing string to JSON
print(json_data)


driver.save_screenshot('resultado.png')

# Cerrar el navegador
driver.quit()

