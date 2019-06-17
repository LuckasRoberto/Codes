from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('nome:')
msg = input('menssagem:')
count = int(input('número:'))

input('qlqr coisa dps do qr code:')

user = driver.find_element_by_xpath('//spam[@title = "{}"]'.format(davi))
user.click()

msg_box = driver.find_element_by_class_name('input-container')

for i in range(count):
	msg_box.send_keys(msg)
	button = driver.find_element_by_class_name('compose-btn-send')