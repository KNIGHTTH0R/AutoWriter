import time
import xlrd
import xlwt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
u_user = "usuario"
u_pass = "senha"
driver = webdriver.Chrome(executable_path=r'C:\Users\(user)\Downloads\Install\chromedriver.exe')
driver.get("site")

#Login
user = driver.find_element_by_id("usuario")
user_pass = driver.find_element_by_id("senha")
user.clear()
user_pass.clear()
user.send_keys(u_user)
user_pass.send_keys(u_pass)
captcha = driver.find_element_by_id("textoVerificador")
print("Digite o captcha: ")
x = input()
captcha.send_keys(x)
user.send_keys(Keys.RETURN)
time.sleep(4)
#Acessar
aces = driver.find_element_by_class_name("lnk-menu-sistema-listagem")
aces.click()
time.sleep(1)
#Relatorio de notas
rel = driver.find_element_by_xpath("//a[@data-ascii='Relatorio de Nota Fiscal                           ']")
rel.click()
time.sleep(1)
#Excel
workbook = xlwt.Workbook()

xlrd.open_workbook()
#http://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
#driver.close()
