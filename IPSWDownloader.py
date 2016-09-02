# coding=utf-8

import urllib2
import json
import time
import requests
import os
import linecache

#####################
debug = "true"
debugUpdater = "false"
velocizza = "true"
version = "v0.1"
#####################

### Individuazione sistema operativo ###
sistemaOperativo = ""

if os.name == "nt":
	sistemaOperativo = "Windows"
else:
	sistemaOperativo = "Unix/Unix-Like"

urlCheckForUpdate = "http://ipswdownloaderpy.altervista.org/nlatest.txt"
if sistemaOperativo == "Unix/Unix-Like":
	os.system("touch /tmp/tmpFileVersione")
	os.system("echo '" + requests.get(urlCheckForUpdate).text + "'" + " > /tmp/tmpFileVersione")
	a = open("/tmp/tmpFileVersione", "r")
else:
	os.system("echo " + requests.get(urlCheckForUpdate).text + " > C:/Windows/Temp/tmpFileVersione")
	a = open("C:/Windows/Temp/tmpFileVersione", "r")


NversioneAggiornata = a.readline(4)

if (NversioneAggiornata == version):
	a.close()
	if sistemaOperativo == "Unix/Unix-Like":
		os.system("rm /tmp/tmpFileVersione")
		time.sleep(1)
	else :
		os.system("rm C:/Windows/Temp/tmpFileVersione")
		time.sleep(1)
	
else:
	vuoiAggiornare = raw_input("È uscita una nuova versione di IPSWDownloader. La vuoi scaricare adesso?")
	if vuoiAggiornare == "Si" or "si" or "yep" or "Yep" or "yes" or "Yes" or "y" or "Y":
		#os.system("rm IPSWDownloader.py")
		os.system("wget http://ipswdownloaderpy.altervista.org/latestVersion.zip")
		os.system("unzip latestVersion.zip")
		os.system("rm latestVersion.zip")
		print ("Apro la nuova versione...")
		time.sleep(3)
		if sistemaOperativo == "Unix/Unix-Like":
			os.system("python IPSWDownloader.py")
			time.sleep(4)
		else:
			os.system("py IPSWDownloader.py")
			time.sleep(4)
		if debugUpdater == "true":
			os.system("rm fileESdaScaricare.zip")
			os.system("touch fileESdaCancellare.py")
		else:
			pass
		a.close()
		os.system("rm /tmp/tmpFileVersione")
		time.sleep(1)
		quit()
	else:
		pass


def velocizzaFunc(sec):
	if velocizza == "true":
		pass
	else:
		time.sleep(sec)


url = "https://api.ipsw.me/v2.1/firmwares.json"
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

device = ""
print ("###### IPSWDownloader v0.1 ######")
print ("###### Sviluppato da Dani Tox ######")
print ("###### Stai utilizzando questo programma su " + sistemaOperativo + " ######")
time.sleep(1.4)
print ("Thanks to ipsw.me for the API/Database")
time.sleep(3)
print ("Ecco tutti i device disponibili e come devono essere scritti:")
time.sleep(2)

print ("iPhone 2G")
velocizzaFunc(0.5)
print ("iPhone 3G")
velocizzaFunc(0.5)
print ("iPhone 3GS")
velocizzaFunc(0.5)
print ("iPhone 4")
velocizzaFunc(0.5)
print ("iPhone 4S")
velocizzaFunc(0.5)
print ("iPhone 5")
velocizzaFunc(0.5)
print ("iPhone 5C")
velocizzaFunc(0.5)
print ("iPhone 5S")
velocizzaFunc(0.5)
print ("iPhone 6")
velocizzaFunc(0.5)
print ("iPhone 6+")
velocizzaFunc(0.5)
print ("iPhone 6S")
velocizzaFunc(0.5)
print ("iPhone 6S+")
velocizzaFunc(0.5)
print ("iPhone SE")
velocizzaFunc(0.5)
print
print ("### iPad ###")
print
velocizzaFunc(0.5)
print ("iPad 1")
velocizzaFunc(0.5)
print ("iPad 2")
velocizzaFunc(0.5)
print ("iPad 3")
velocizzaFunc(0.5)
print ("iPad 4")
velocizzaFunc(0.5)
print ("iPad Air")
velocizzaFunc(0.5)
print ("iPad Air 2")
velocizzaFunc(0.5)
print ("iPad Mini")
velocizzaFunc(0.5)
print ("iPad Mini 2")
velocizzaFunc(0.5)
print ("iPad Mini 3")
velocizzaFunc(0.5)
print ("iPad Mini 4")
velocizzaFunc(0.5)
print ('iPad Pro 9.7"')
velocizzaFunc(0.5)
print ('iPad Pro 12.9"')
velocizzaFunc(0.5)
print
print ("### iPod ###")
print 
velocizzaFunc(0.5)
print ("iPod Touch 1G")
velocizzaFunc(0.5)
print ("iPod Touch 2G")
velocizzaFunc(0.5)
print ("iPod Touch 3G")
velocizzaFunc(0.5)
print ("iPod Touch 4G")
velocizzaFunc(0.5)
print ("iPod Touch 5G")
velocizzaFunc(0.5)
print ("iPod Touch 6G")
velocizzaFunc(0.5)
print
print ("### Apple TV ###")
print
velocizzaFunc(0.5)
print ("Apple TV 2")
velocizzaFunc(0.5)
print ("Apple TV 3")
velocizzaFunc(0.5)
print ("Apple TV 4")
print

deviceRichiesto = raw_input("Scrivi l'iDevice che ti serve: ")


########################################################################################################################


####		iPhones			#####

if deviceRichiesto == "iPhone 2G":
	device = "iPhone1,1"
elif deviceRichiesto == "iPhone 3G":
	device = "iPhone1,2"
elif deviceRichiesto == "iPhone 3GS":
	device = "iPhone2,1"
elif deviceRichiesto == "iPhone 4":
	print("Quale modello di iPhone 4 intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) GSM")
	print ("2) GSM/2012")
	print ("3) CDMA")
	mdliph4 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdliph4 == 1:
		device = "iPhone3,1"
	elif mdliph4 == 2:
		device = "iPhone3,2"
	elif mdliph4 == 3:
		device = "iPhone3,3"

elif deviceRichiesto == "iPhone 4S":
	device = "iPhone4,1"
elif deviceRichiesto == "iPhone 5":
	print("Quale modello di iPhone 5 intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) GSM")
	print ("2) Global")
	mdliph5 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdliph5 == 1:
		device = "iPhone5,1"
	elif mdliph5 == 2:
		device = "iPhone5,2"

elif deviceRichiesto == "iPhone 5C":
	print("Quale modello di iPhone 5C intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) GSM")
	print ("2) Global")
	mdliph5c = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdliph5c == 1:
		device = "iPhone5,3"
	elif mdliph5c == 2:
		device = "iPhone5,4"
elif deviceRichiesto == "iPhone 6":
	device = "iPhone7,2"
elif deviceRichiesto == "iPhone 6+":
	device = "iPhone7,1"
elif deviceRichiesto == "iPhone 6s":
	device = "iPhone8,1"
elif deviceRichiesto == "iPhone 6s+":
	device = "iPhone8,2"
elif deviceRichiesto == "iPhone SE":
	device = "iPhone8,4"

#####		iPads			####

elif deviceRichiesto == "iPad 1":
	device = "iPad1,1"
elif deviceRichiesto == "iPad 2":
	print("Quale modello di iPad 2 intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) iPad 2 (WiFi)")
	print ("2) iPad 2 (GSM)")
	print ("3) iPad 2 (CDMA)")
	print ("4) iPad 2 (Mid 2012)")
	mdlipa2 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipa2 == 1:
		device = "iPad2,1"
	elif mdlipa2 == 2:
		device = "iPad2,2"
	elif mdlipa2 == 3:
		device = "iPad2,3"
	elif mdlipa2 == 4:
		device = "iPad2,4"
elif deviceRichiesto == "iPad 3":
	print("Quale modello di iPad 3 intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) iPad 3 (WiFi)")
	print ("2) iPad 3 (CDMA)")
	print ("3) iPad 3 (GSM)")
	mdlipa3 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipa3 == 1:
		device = "iPad3,1"
	elif mdlipa3 == 2:
		device = "iPad3,2"
	elif mdlipa3 == 3:
		device = "iPad3,3"
elif deviceRichiesto == "iPad 4":
	print("Quale modello di iPad 4 intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) iPad 4 (WiFi)")
	print ("2) iPad 4 (GSM)")
	print ("3) iPad 4 (Global)")
	mdlipa4 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipa4 == 1:
		device = "iPad3,4"
	elif mdlipa4 == 2:
		device = "iPad3,5"
	elif mdlipa4 == 3:
		device = "iPad3,6"
elif deviceRichiesto == "iPad Air":
	print("Quale modello di iPad Air intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) iPad Air (WiFi)")
	print ("2) iPad Air (Cellular)")
	print ("3) iPad Air (China)")
	mdlipaA = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipaA == 1:
		device = "iPad4,1"
	elif mdlipaA == 2:
		device = "iPad4,2"
	elif mdlipaA == 3:
		device = "iPad4,3"
elif deviceRichiesto == "iPad Air 2":
	print ("Quale modello di iPad Air 2 intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) iPad Air 2 (WiFi)")
	print ("2) iPad Air 2 (Cellular)")
	mdlipaA2 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipaA2 == 1:
		device = "iPad5,3"
	elif mdlipaA2 == 2:
		device = "iPad5,4"
elif deviceRichiesto == "iPad Mini":
	print("Quale modello di iPad Mini intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) iPad Mini (WiFi)")
	print ("2) iPad Mini (GSM)")
	print ("3) iPad Mini (Gloabl)")
	mdlipam = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipam == 1:
		device = "iPad2,5"
	elif mdlipam == 2:
		device = "iPad2,6"
	elif mdlipam == 3:
		device = "iPad2,7"
elif deviceRichiesto == "iPad Mini 2":
	print("Quale modello di iPad Mini 2 intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) iPad Mini 2 (WiFi)")
	print ("2) iPad Mini 2 (Cellular)")
	print ("3) iPad Mini 2 (China)")
	mdlipam2 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipam2 == 1:
		device = "iPad4,4"
	elif mdlipam2 == 2:
		device = "iPad4,5"
	elif mdlipam2 == 3:
		device = "iPad4,6"
elif deviceRichiesto == "iPad Mini 3":
	print ("Quale modello di iPad Mini 3 intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) iPad Mini 3 (WiFi)")
	print ("2) iPad Mini 3 (Cellular)")
	print ("3) iPad Mini 3 (China)")
	mdlipam3 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipam3 == 1:
		device = "iPad4,7"
	elif mdlipam3 == 2:
		device = "iPad4,8"
	elif mdlipam3 == 3:
		device = "iPad4,9"
elif deviceRichiesto == "iPad Mini 4":
	print ("Quale modello di iPad Mini 4 intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) iPad Mini 4 (WiFi)")
	print ("2) iPad Mini 4 (Cellular)")
	mdlipam4 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipam4 == 1:
		device = "iPad5,1"
	elif mdlipam4 == 2: 
		device = "iPad5,2"
elif deviceRichiesto == 'iPad Pro 9.7"':
	print ('Quale modello di iPad Pro 9.7" intendi? Fra poco appariranno quelli disponibili:')
	velocizzaFunc(3)
	print ('1) iPad Pro 9.7" (WiFi)')
	print ('2) iPad Pro 9.7" (Cellular)')
	mdlipap9 = raw_input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipap9 == 1:
		device = "iPad6,3"
	elif mdlipap9 == 2: 
		device = "iPad6,4"
elif deviceRichiesto == 'iPad Pro 12.9"':
	print ('Quale modello di iPad Pro 12.9" intendi? Fra poco appariranno quelli disponibili:')
	velocizzaFunc(3)
	print ('1) iPad Pro 12.9" (WiFi)')
	print ('2) iPad Pro 12.9" (Cellular)')
	mdlipap12 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlipap12 == 1:
		device = "iPad6,7"
	elif mdlipap12 == 2:
		device = "iPad6,8"

####		iPod		####

elif deviceRichiesto == "iPod Touch 1G":
	device = "iPod1,1"
elif deviceRichiesto == "iPod Touch 2G":
	device = "iPod2,1"
elif deviceRichiesto == "iPod Touch 3G":
	device = "iPod3,1"
elif deviceRichiesto == "iPod Touch 4G":
	device = "iPod4,1"
elif deviceRichiesto == "iPod Touch 5G":
	device = "iPod5,1"
elif deviceRichiesto == "iPod Touch 6G":
	device = "iPod7,1"

####		Apple TV		####

elif deviceRichiesto == "Apple TV 2":
	device = "AppleTV2,1"
elif deviceRichiesto == "Apple TV 3":
	print ("Quale modello di Apple TV 3 intendi? Fra poco appariranno quelli disponibili:")
	velocizzaFunc(3)
	print ("1) Apple TV 3")
	print ("2) Apple TV 3 (2013)")
	mdlatv3 = input("Scrivi il numero scritto a sinistra del modello che intendi: ")
	if mdlatv3 == 1:
		device = "AppleTV3,1"
	elif mdlatv3 == 2:
		device = "AppleTV3,2"
elif deviceRichiesto == "Apple TV 4":
	device = "AppleTV5,3"

else:
	print("Errore! Probabilmente hai sbagliato a scrivere il device")


############################################################################################################

n = 0
while n < len(data["devices"][device]["firmwares"]) :
	print (str(n) + ") " + data["devices"][device]["firmwares"][n]["version"])
	n += 1


versioneScelta = input("Ecco le versioni di iOS disponibili per questo dispsitivo. Scrivi il numero a sinistra della versione che vuoi: ")

x = 0

while x < 50 :
	if x == versioneScelta:
		print
		print ("Hai scelto iOS " + data["devices"][device]["firmwares"][x]["version"])
		break
	x += 1

urlDownload = data["devices"][device]["firmwares"][x]["url"]

print 
print (u"Ecco l'URL da cui scaricherò il file IPSW: " + urlDownload)
print

time.sleep(3)

print ("Sto iniziando a scaricare...")
print
print ("Prmi ctrl + C per interrompere")
print

os.system("wget " + urlDownload)

if debug == "true":
	print
	print ("Debug Message: ")
	vuoiCancellare = raw_input("Visto che questa è una versione in fase di sviluppo, vuoi cancellare il file appena scaricato? ")
	if vuoiCancellare == "Si" or "si" or "Yep" or "Yes":
		os.system("rm " + data["devices"][device]["firmwares"][x]["filename"])
		print ("Cancellato :)")
		time.sleep(1)
		print ("Chiudo il programma...")
		time.sleep(1.5)
	else:
		pass
else:
	pass









