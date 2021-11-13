from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time, datetime, os
from datetime import date
import datetime as dt
from datetime import datetime
import pandas as pd
import warnings
from urllib.parse import urlparse
from time import sleep
import random
from selenium.webdriver.chrome.options import Options
warnings.filterwarnings("ignore", category=DeprecationWarning) 


#start_time = time.time()
#now = dt.datetime.now()
#print('Início = ',now.strftime("%d/%m/%Y, %H:%M:%S"))

while True:
    chrome_options = Options() 
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    # Definindo as configurações de data/hora e definindo o diretório
    data = datetime.now()
    hoje = data.strftime("%d-%m-%Y")
    hora = data.strftime("%H_%M")

    # Criando diretórios 
    try:
        os.makedirs('./IMG/google_maps_traffic/'+ hoje + '/' + hora + '/')
    except FileExistsError:
        pass
        continue
        
    # txt com a lista das urls das cenas
    lista = open("urls.txt", "r").readlines()[0:80]

    # Passando os links e salvando os screenshots
    try:
        for i, url in enumerate(lista):
            driver.get(url)
            driver.get_screenshot_as_file('./IMG/google_maps_traffic/'+ hoje + '/' + hora + '/' + 'folha_{}.png'.format(i + 1))
    except FileExistsError:
        pass
    
   
    driver.quit()

    #print("Tempo de processamento foi de %g segundos." % (time.time() - start_time))
    time.sleep(6*60)