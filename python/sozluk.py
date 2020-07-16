from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
import time
from IPython.display import display
import requests
from os import system, name
import webbrowser
from signal import signal, SIGINT
from sys import exit

def sor_func():
	ayarlar = webdriver.ChromeOptions()
	ayarlar.add_argument('headless')
	girdi = 1
	sayi = 0
	driverK0num = open('gerekli/chr_drv_yol.txt')
	hlp = open('benioku.txt')
	kok = '-i'
	kelime = input('\033[1;35m Aranacak olan (Atasözü, kelime, vb.): \033[97m')
	bol = kelime.split()
	if kelime in {'çık', 'Çık', 'ÇIK', '99', 'exit'}:
		exit()
	if kok in bol:
		x = kelime.replace('-i', '')
		print('\n\n')
		url = 'https://sozluk.gov.tr'
		driver = webdriver.Chrome(driverK0num.read().replace('\n', ''), options=ayarlar)
		driver.get(url)
		driver.find_element_by_id('tdk-srch-input').send_keys(x)
		driver.find_element_by_id('tdk-search-btn').click()
		time.sleep(girdi)
		html = driver.page_source
		spdrsrc = BeautifulSoup(html, 'html.parser')
		anlam = None
		anlam = spdrsrc.find('div', {'id':'ozellikler-gts0'})
		if anlam != None:
			if anlam.text == ' ':
				print('----------------------------------------\n')
				print('Özellik bilgisi bulunmamaktadır. \033[38;5;198m(Köken Türkçe olabilir)\033[97m\n')
				print('----------------------------------------\n\n\n')
			else:
				print('----------------------------------------\n')
				print('\033[38;5;198m', anlam.text,'\033[97m', '\n')
				print('----------------------------------------\n\n\n')
		else:
			print('Böyle bir kelime bulunamadı.\n\n\n')
	if kelime == '/gününkelimesi':
		gunKel_func()
	if kelime == '/gününsözü':
		gunAt_func()
	if kelime == '/d':
		detaylı_func()
	if kelime in {'help', '-h'}:
		print('\n',hlp.read(), '\n\n')
	if kelime == 'clear':
		clear()
	if kelime != '' and kelime != '/gününkelimesi' and kelime != '/gününsözü' and kelime != 'clear' and kok not in bol and kelime not in {'help', '-h'} and kelime != '/d':
		url = 'https://sozluk.gov.tr'
		driver = webdriver.Chrome(driverK0num.read().replace('\n', ''), options=ayarlar)
		driver.get(url)
		driver.find_element_by_id('tdk-srch-input').send_keys(kelime)
		driver.find_element_by_id('tdk-search-btn').click()
		time.sleep(girdi)
		html = driver.page_source
		spdrsrc = BeautifulSoup(html, 'html.parser')
		hoo = BeautifulSoup(html, 'html.parser')
		tag = BeautifulSoup(html, 'html.parser')
		anlam = None
		for hoo in spdrsrc.find_all('div', {'id':'anlamlar-gts0'}):
			anlam = hoo.find_all('p')
		for tag in hoo.find_all('p'):
			sayi=sayi+1
		print('\n\n')
		if anlam != None :
			print('-----------------------------------------------------------------------------------------')
			if sayi == 1 :
				print(anlam[0].text)
			elif sayi == 2 :
				print(anlam[0].text, anlam[1].text, sep="\n\n")
			elif sayi == 3 :
				print(anlam[0].text, anlam[1].text, anlam[2].text, sep="\n\n")
			elif sayi == 4 :
				print(anlam[0].text, anlam[1].text, anlam[2].text, anlam[3].text, sep="\n\n")
			elif sayi == 5 :
				print(anlam[0].text, anlam[1].text, anlam[2].text, anlam[3].text, anlam[4].text, sep="\n\n")
			elif sayi == 6 :
				print(anlam[0].text, anlam[1].text, anlam[2].text, anlam[3].text, anlam[4].text, anlam[5].text, sep="\n\n")
			elif sayi > 6 :
				print(anlam[0].text, anlam[1].text, anlam[2].text, anlam[3].text, anlam[4].text, anlam[5].text,'\033[1;34mAradığınızın altıdan fazla anlamı var. Devamı için "https://sozluk.gov.tr" adresini ziyaret edin.\nGösterilecek anlam sayısının artmasını istiyorsanız bana ulaşabilirsiniz.\033[97m', sep="\n\n")
			print('-----------------------------------------------------------------------------------------')
			print('\n\n')
		else:
			print('Aradığınız bulunamadı.\nVirgül kullandığınızdan ve doğru yazdığınızdan emin olun.')
			print('\n\n')
			arama_onay = input('Detaylı aramak ister misiniz?')
			if arama_onay in {'Evet', 'evet', 'y', 'Y'}:
				detaylı_func()

def detaylı_func():
	ayarlar = webdriver.ChromeOptions()
	ayarlar.add_argument('headless')
	girdi = 10
	sayi = 0
	driverK0num = open('gerekli/chr_drv_yol.txt')
	hlp = open('benioku.txt')
	kelime = input('\033[1;35m Detaylı aranacak olan (Atasözü, kelime, vb.): \033[97m')
	if kelime in {'çık', 'Çık', 'ÇIK', '99', 'exit'}:
		exit()
	if kelime == '/gününkelimesi':
		gunKel_func()
	if kelime == '/gününsözü':
		gunAt_func()
	if kelime in {'help', '-h'}:
		print(hlp.read())
	if kelime == 'clear':
		clear()
	if kelime != '' and kelime != '/gününkelimesi' and kelime != '/gününsözü' and kelime != 'clear' and kelime not in {'help', '-h'}:
		url = 'https://sozluk.gov.tr'
		driver = webdriver.Chrome(driverK0num.read().replace('\n', ''), options=ayarlar)
		driver.get(url)
		driver.find_element_by_id('tdk-srch-input').send_keys(kelime)
		driver.find_element_by_id('tdk-search-btn').click()
		time.sleep(girdi)
		html = driver.page_source
		spdrsrc = BeautifulSoup(html, 'html.parser')
		hoo = BeautifulSoup(html, 'html.parser')
		tag = BeautifulSoup(html, 'html.parser')
		anlam = None
		for hoo in spdrsrc.find_all('div', {'id':'anlamlar-gts0'}):
			anlam = hoo.find_all('p')
		for tag in hoo.find_all('p'):
			sayi=sayi+1
		print('\n\n')
		if anlam != None :
			print('-----------------------------------------------------------------------------------------')
			if sayi == 1 :
				print(anlam[0].text)
			elif sayi == 2 :
				print(anlam[0].text, anlam[1].text, sep="\n\n")
			elif sayi == 3 :
				print(anlam[0].text, anlam[1].text, anlam[2].text, sep="\n\n")
			elif sayi == 4 :
				print(anlam[0].text, anlam[1].text, anlam[2].text, anlam[3].text, sep="\n\n")
			elif sayi == 5 :
				print(anlam[0].text, anlam[1].text, anlam[2].text, anlam[3].text, anlam[4].text, sep="\n\n")
			elif sayi == 6 :
				print(anlam[0].text, anlam[1].text, anlam[2].text, anlam[3].text, anlam[4].text, anlam[5].text, sep="\n\n")
			elif sayi > 6 :
				print(anlam[0].text, anlam[1].text, anlam[2].text, anlam[3].text, anlam[4].text, anlam[5].text,'\033[1;34mAradığınızın altıdan fazla anlamı var. Devamı için "https://sozluk.gov.tr" adresini ziyaret edin.\nGösterilecek anlam sayısının artmasını istiyorsanız bana ulaşabilirsiniz.\033[97m', sep="\n\n")

			print('-----------------------------------------------------------------------------------------')
			print('\n\n')
		else:
			print('Aradığınız bulunamadı.\nVirgül kullandığınızdan ve doğru yazdığınızdan emin olun.')
			print('\n\n')

def gunKel_func():
	driverK0num = open('gerekli/chr_drv_yol.txt')
	ayarlar = webdriver.ChromeOptions()
	ayarlar.add_argument('headless')
	sayi = 0
	url = 'https://sozluk.gov.tr'
	driver = webdriver.Chrome(driverK0num.read().replace('\n', ''), options=ayarlar)
	driver.get(url)
	html = driver.page_source
	spdrsrc = BeautifulSoup(html, 'html.parser')
	hoo = BeautifulSoup(html, 'html.parser')
	tag = BeautifulSoup(html, 'html.parser')
	kel = None
	for hoo in spdrsrc.find_all('table', {'class':'kelime'}):
		kel = hoo.find_all('tr')
	for tag in hoo.find_all('tr'):
		sayi=sayi+1
	print('\n\n')
	if kel != None :
		print('-----------------------------------------------------------------------------------------')
		if sayi == 1 :
			print('\033[38;5;198m', kel[0].text, '\033[97m')
		elif sayi == 2 :
			print('\033[38;5;198m', kel[0].text, '\033[97m', kel[1].text, sep="\n")
		elif sayi == 3 :
			print('\033[38;5;198m', kel[0].text, '\033[97m', kel[1].text, kel[2].text, sep="\n")

		print('\n')
		print('-----------------------------------------------------------------------------------------')
		print('\n\n')
	else:
		print('Bu hata mesajını görüyorsanız bilmediğim bir sorunla karşı karşıyasınız demektir.')
		print('\n\n')

def gunAt_func():
	driverK0num = open('gerekli/chr_drv_yol.txt')
	ayarlar = webdriver.ChromeOptions()
	ayarlar.add_argument('headless')
	url = 'https://sozluk.gov.tr'
	driver = webdriver.Chrome(driverK0num.read().replace('\n', ''), options=ayarlar)
	driver.get(url)
	html = driver.page_source
	spdrsrc = BeautifulSoup(html, 'html.parser')
	at = None
	atAnlam = None
	at = spdrsrc.find('p', {'class':'atasoz0'})
	atAnlam = spdrsrc.find('span', {'class':'atasozAnlam0'})
	print('\n\n')
	if at != None :
		print('-----------------------------------------------------------------------------------------')
		print('\033[38;5;198m', at.text, '\033[97m', atAnlam.text, sep="\n")
		print('\n')
		print('-----------------------------------------------------------------------------------------')
		print('\n\n')
	else:
		print('Bu hata mesajını görüyorsanız bilmediğim bir sorunla karşı karşıyasınız demektir.')
		print('\n\n')

def ctrlcFunc(signal_received, frame):
	print('\n\n\nHoşça kal\n\n')
	exit()

if __name__ == '__main__':
	signal(SIGINT, ctrlcFunc)

def clear():
	system('clear')

while True:
	sor_func()

# Not: Gününkelimesinin, birden fazla anlamı olunca boşluk görünüyor.