from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from twilio.rest import Client 

s=Service('CHROMEDRIVER-LOCATION')
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(service=s, options=options)
url='GOOGLE PAGE FOR YOUR STOCK' # simply type in the name of the stock you want to track in google and copy the url from the search bar and paste it here

driver.get(url)
time.sleep(2)
stock_name = driver.find_element('xpath', '//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[1]/div/div/span').text
price = driver.find_element('xpath', '//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]')

stock_price = float(price.text)
shares_owned = 0 # REPLACE WITH THE NUMBER OF SHARES YOU OWN

whole = stock_price * shares_owned
total = round(whole, 2)
total_rounded = '${:,.2f}'.format(total)

account_sid = 'TWILIO ACCOUNT SID' 
auth_token = 'AUTH TOKEN' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MESSAGING SERVICE SID', 
                              body=stock_name + ' stock is currently at ' + price.text + ' per share. You have ' + str(shares_owned) + ' shares. Your total is ' + total_rounded + '.',
                              to='+ YOUR PHONE NUMBER' 
                          ) 
 
print(message.sid)
