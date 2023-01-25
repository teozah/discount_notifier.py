

import smtplib
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


global mail_sent
mail_sent = False

def check_price():
    
    url = "https://sneakerindustry.ro/ro/imbracaminte-barbati/12723-73290-made-in-usa-nrg-crewneck.html#/184-marime-s"
    
    driver = webdriver.Chrome()

    driver.get(url)

    # wait for page
    time.sleep(5)

    # find the price element
    price_element = driver.find_element(By.XPATH, '//*[@itemprop="price"]')

    # get the text
    price = price_element.text

    print(price)
    
    # format the price to only numbers
    float_price = re.sub("[^0-9.]", "", price)
    print(f"Pretul actual: {float_price}")
    
    # Set the desired price threshold
    threshold = str(20000) #200.00 Lei
    # If the price is lower than the threshold, send an email
    if float_price < threshold:
        send_email()
        global mail_sent
        mail_sent = True
    driver.close()

def send_email():

    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    server.login('sneakersbotro@gmail.com', 'cfdqcucebhznzppb')
    
    subject = "!!!REDUCERE!!!"
    body = "Vezi aici reducerea: https://sneakerindustry.ro/ro/imbracaminte-barbati/12723-73290-made-in-usa-nrg-crewneck.html#/184-marime-s"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('sneakersbotro@gmail.com', "teo_tzt@yahoo.com", msg)
    print("Email has been sent!")
    server.quit()


# check price every 1 hour
while not mail_sent:
    print(mail_sent)
    check_price()
    time.sleep(60 * 60)
