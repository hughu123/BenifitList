# Hugo Humble
# 2024-07-28
# Version 1.0

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import csv as csv
import easygui as eg

def start_up():
    
    username = ""
    password = ""
    
    while(True):
        username = eg.enterbox("Enter username: ", "Login")
        password = eg.passwordbox("Enter password: ", "Login")   
        if username == "":
            eg.exceptionbox("You didn't enter a username, please try again.","Failed to enter username")
            continue
        elif  password == "":
            eg.exceptionbox("You didn't enter a password, please try again.","Failed to enter password")
            continue
        else:
            break

    return username, password 









# Starta en webbläsarsession med Edge
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))


try:

   ##################
   # ATT GÖRA LISTA #
   ##################
   # 
   # [] Skapa fler popup-rutor för simpel användning
   #
   # [] Förenkla kod struktur med definerade funktioner istället
   #








    ##################
    # Login Sequence #
    ##################
    # Gå till inloggningssidan
    driver.get("https://personal.trappan.nu/login.php")

    # Hitta och fyll i användarnamn och lösenord
    username_field = driver.find_element(By.NAME, "user_name")
    password_field = driver.find_element(By.NAME, "password")

    # username = eg.enterbox("Användarnamn: ")
    # password = eg.passwordbox("Lösenord: ")

    username, password = start_up()

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Klicka på inloggningsknappen
    login_button = driver.find_element(By.NAME, "log_in")
    login_button.click()

    # Vänta tills du är inloggad
    time.sleep(1)

    #####################
    # Benefits Sequence #
    #####################

    # Gå till förmånssidan
    # driver.get("https://personal.trappan.nu/index.php?page=periodBenefits&period=105")
    driver.get("https://personal.trappan.nu/index.php?page=periodBenefits&period=106")

    #Hämtar sidans källkod
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Filtrerar personalens url till inviduella profiler
    tbody = soup.find("tbody")
    # print(tbody)

    a_tags = tbody.find_all('a')

    # Lägger till bas url:n till listan för enkelhetens skull
    base_url = "https://personal.trappan.nu/index.php"
    hrefs = [base_url + a.get('href') for a in a_tags]

    print(hrefs) # for debugging

    ####################
    # Email Extraction #
    ####################

    list_of_emails = []

    for profil in hrefs:
        driver.get(profil)
        email = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/div/div[2]/table/tbody/tr[1]/td[2]').text
        list_of_emails.append(email)
        
    print(list_of_emails)

   



    

    
   

finally:
    # Avsluta webbläsarsessionen
    driver.quit()




