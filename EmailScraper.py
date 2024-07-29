# Hugo Humble
# 2024-07-28
# Version 1.1



    ##################
    # ATT GÖRA LISTA #
    ##################
    # 
    # [] Skapa fler popup-rutor för "informativ" användning
    #
    # [] Förenkla kod struktur med definerade funktioner istället
    #
    # [] Sortera email i två grupper, Guld och Silver-förmåner
    #
    #
    #

###################
# Libs to install #
###################

# pip install beautifulsoup4
from bs4 import BeautifulSoup 

# pip install selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

#pip install webdriver-manager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time
import csv as csv
import easygui as eg

#############
# Functions #
#############

def login_sequence():

    eg.exceptionbox("Make sure that you enter your login information correct, no \"try/catch\" has been implemented for incorrect login as of yet","Crucial message for End-User")
    
    username = ""
    password = ""

    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    
    driver.get("https://personal.trappan.nu/login.php")

    username_field = driver.find_element(By.NAME, "user_name")
    password_field = driver.find_element(By.NAME, "password")
    
    while(True):
        username = eg.enterbox("Enter username: ", "Login")
        username_field.send_keys(username)
        password = eg.passwordbox("Enter password: ", "Login")  
        password_field.send_keys(password) 
        if username == "":
            eg.exceptionbox("You didn't enter a username, please try again.","Failed to enter username")
            continue
        elif  password == "":
            eg.exceptionbox("You didn't enter a password, please try again.","Failed to enter password")
            continue
        else:
            # add case if login fails
            # try:
                login_button = driver.find_element(By.NAME, "log_in")
                login_button.click()

                
            
            # finally:
                break

    return username, password, driver

try:

    ##################
    # Login Sequence #
    ##################
    
    # print("Before fetch_email()") # debugging

    username, password, driver = login_sequence()

    # Ensure login success
    time.sleep(1)

    # print("After fetch_email()") # debugging

    #####################
    # Benefits Sequence #
    #####################

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

    # print(hrefs) # for debugging

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




