from selenium import webdriver
from time import sleep 

url = "https://web.whatsapp.com/"
options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument(r"user-data-dir=C:/Users/uriel/Documents/Python/Project #4/temp")

d = webdriver.Chrome('C:/Users/uriel/Documents/Python/Project #4/chromedriver.exe',chrome_options=options)
d.get(url)
sleep(6)

contact = []
try:
    people_name = d.find_elements_by_class_name("_3TEwt")
    for p_name in people_name:
        contact.append(str(p_name.text))
except:
    pass
try:
    people_name = d.find_elements_by_class_name("_25Ooe")
    for p_name in people_name:
        contact.append(str(p_name.text))
except:
    pass

try:
    people_name = d.find_elements_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[15]/div/div/div[2]/div[1]/div[1]/span/span')
    for p_name in people_name:
        contact.append(str(p_name.text))
except:
    pass

print(contact)
print("Here's your contacts:\nChose a number respective of your contact on menu bellow\n")
counter = 0
for a in contact:
    print(str(counter)+" "+a)
    counter = counter+1
targ_contact = int(input())
target = d.find_element_by_xpath('//span[@title = "{}"]'.format(str(contact[targ_contact])))
target.click()

messagetext = str(" ")

while messagetext != "done":
    messagetext = str(input("[Mensagem:]\n" ))
    if messagetext=="done":
        exit()
    sleep(4)
    text_Box = d.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    text_Box.click()

    sleep(1)

    text_Box.send_keys(str(messagetext))

    press_Enter = d.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
        
    sleep(1)
    press_Enter.click()
