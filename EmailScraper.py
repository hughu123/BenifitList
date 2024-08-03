# Hugo Humble
# 2024-08-03
# Version 1.3


    ##################
    # ATT GÖRA LISTA #
    ##################
    # 
    # [75%] Skapa fler popup-rutor för "informativ" användning
    #
    # [50%] Förenkla kod struktur med definerade funktioner istället
    #
    # [100%] Sortera email i två grupper, Guld och Silver-förmåner
    #
    # [100%] Skapa en csv fil med mailadresserna
    #       [???] Välja att skapa listor med olika filter (som guld och silver separat)
    #
    # 
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

# Test
from itertools import zip_longest



#############
# Functions #
#############

def login_sequence(mydriver):
    message = load_text()
    # print(message) # debugging
    eg.exceptionbox(message,"Before using the program") # message for user
    
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

        # Försök logga in på hemsidan med angivna uppgifter
        username = eg.enterbox("Enter username: ", "Login")
        username_field.send_keys(username)
        password = eg.passwordbox("Enter password: ", "Login")  
        password_field.send_keys(password)

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

def csvMaker(list): # WIP
    benefits = []
    titel_namn = ['Namn','Poäng','Profil','Email']

    return benefits

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

    ###########
    ### Add state that checks the entered website of being a correct one
    ###########
    
    benifit_url = eg.enterbox("Enter the URL of the benefit you want to calculate\nHeres an example of an URL: \n\"https://personal.trappan.nu/index.php?page=periodBenefits&period=105\" ","Please enter the URL of the benefit page")
    driver.get(benifit_url)
    # driver.get("https://personal.trappan.nu/index.php?page=periodBenefits&period=106")

    # Hämtar sidans källkod
    soup = BeautifulSoup(driver.page_source,"html5lib")
    
    # Email extrahering och text manipulering
    tbody = soup.find("tbody")
    names = []
    benifits = []

    personal = tbody.getText("\n",True)
    lines = personal.splitlines()

    for item in range(0,len(lines),2):
        name = lines[item]
        benifit = lines[item + 1]

        names.append(name)
        benifits.append(benifit)

    a_tags = tbody.find_all('a')
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
    

    tiers = []
    for status in benifits:
        if status == '1x + 0x' or status == '0x + 1x':
            tier = 'Silver'
            tiers.append(tier)

        else:
            tier = 'Guld'
            tiers.append(tier)

    # print(tiers) # debugging

    
    if len(names) == len(hrefs) and len(benifits) == len(hrefs) and len(list_of_emails) == len(hrefs) and len(tiers) == len(hrefs): 
        # wtf is this if statement smh...
        print('All lists contain an equal amount, OK')
        
        with open('test.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
    
            # Write the headers
            writer.writerow(["Name", "Poäng", "Email", "Förmåner"])
            
            # Write the data rows
            for n, p, e, f in zip(names, benifits, list_of_emails, tiers):
                writer.writerow([n, p, e, f])
            csv_file.close()

    else:
        print('Issues with lists being different sizes, ERROR')



finally:
    # Avsluta webbläsarsessionen
    driver.quit()




