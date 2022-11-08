from numpy import True_
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Controlador web
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Definir el método de extracción de datos para Exoplanet
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## AGREGAR EL CÓDIGO AQUÍ ##
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for i in soup.find_all("nul",attrs={"class","exoplanets"}):
            lee=i.find_all("li")
            tempList=[]
            for j,h in enumerate(lee):
                if j==0:
                    tempList.append(h.find_all("a"),[0].contents[0])
                else:
                    try:
                         tempList.append(h.contents[0])    
                    except:
                        tempList.append("")
            planets_data.ppend(tempList)
        
        browser.find_element(by=By.XPATH,value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            
                 
                
             



        
# Llamada del método
scrape()

# Definir los encabezados
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Definir el dataframe de Pandas
dataExo=pd.DataFrame(planets_data,columns=headers)

# Convertir a CSV
dataExo.to_csv('DataF.csv',index=True,index_label="id")
    


