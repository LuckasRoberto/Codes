from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

#name = input('name: ')
msg = str(input('mensagem:'))
qnt = int(input('quantidade:'))

lista_de_nomes = ['marcus']
lista_de_numeros = [558597913114, 558587386486]

def spam_por_nome(msg):
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    txt_box = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

    for i in range(qnt):
        txt_box.send_keys(msg)
        b = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[3]/button')
        b.click()


def spam_por_numero(phone_no, msg):
     user2 = driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
     user2.click()


     txt_box = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')


     for i in range(qnt):
      txt_box.send_keys(msg)
      b = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[3]/button')
      b.click()

for name in lista_de_nomes:
    spam_por_nome(msg)
