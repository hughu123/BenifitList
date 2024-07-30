# Hugo Humble
# 2024-07-30
# Version 1.2


    ##################
    # ATT GÖRA LISTA #
    ##################
    # 
    # [75%] Skapa fler popup-rutor för "informativ" användning
    #
    # [50%] Förenkla kod struktur med definerade funktioner istället
    #
    # [] Sortera email i två grupper, Guld och Silver-förmåner
    #
    # [] Skapa en csv fil med mailadresserna
    #       [] Välja att skapa listor med olika filter (som guld och silver separat)
    #
    # [] 
    #

###################
# Libs to install #
###################

# pip install beautifulsoup4
from bs4 import BeautifulSoup # kanske inte ens behövs! (kolla vidare på detta...)

# pip install selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

#pip install webdriver-manager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time
import csv as csv

# pip install easygui
import easygui as eg

from config import myUsername, myPassword



#############
# Functions #
#############

def login_sequence(mydriver):
    message = load_text()
    # print(message) # debugging
    eg.exceptionbox(message,"Before using the program")

    # driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    
    login_test(mydriver)

    # return driver

def load_text():
    text_file = ""
    with open("message.txt","r") as f:
        text_file = f.read()
        f.close()
    
    return text_file


def login_test(driver):
    print("Starting login_test()") # debugging

    # Gå till Trappas hemsida
    driver.get("https://personal.trappan.nu/login.php")

    

    while True:
        # Hitta fält
        username_field = driver.find_element(By.NAME, "user_name")
        password_field = driver.find_element(By.NAME, "password")

        # # Försök logga in på hemsidan med angivna uppgifter
        # username = eg.enterbox("Enter username: ", "Login")
        # username_field.send_keys(username)
        # password = eg.passwordbox("Enter password: ", "Login")  
        # password_field.send_keys(password)
        username_field.send_keys(myUsername)
        password_field.send_keys(myPassword)

        login_button = driver.find_element(By.NAME, "log_in")
        login_button.click()

        # Kontrollera inloggningsuppgifter
        if driver.current_url == "https://personal.trappan.nu/login.php":
                print("Loggin failed")
                eg.exceptionbox("Ditt användarnamn eller lösenord var fel, vänligen försök igen!")
                continue
        else:
             break
    print("login_test() ran successfully") # debugging

    
 


try:

    ##################
    # Login Sequence #
    ##################

    ## Starta webdriver
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    login_sequence(driver)

    #####################
    # Benefits Sequence #
    #####################


    # driver.get("https://personal.trappan.nu/index.php?page=periodBenefits&period=105")
    driver.get("https://personal.trappan.nu/index.php?page=periodBenefits&period=106")

    # Hämtar sidans källkod
    soup = BeautifulSoup(driver.page_source,"html5lib")

    # print("soup.text")
    # print(soup.text)

    # # for debugging
    # text_file = open(r"benefit_page.txt", "w")
    # text_file.write(soup.text)
    # text_file.close()
    
    
    # Email extrahering och text manipulering
    tbody = soup.find("tbody")
    print("tbody")
    print(tbody.getText(" \n", True))
    a_tags = tbody.find_all('a')
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
        
    print(list_of_emails) # Sorterade i ingående ordning från den genererade förmånslistan på portalen


finally:
    # Avsluta webbläsarsessionen
    driver.quit()




