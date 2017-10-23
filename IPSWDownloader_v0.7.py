# coding=utf-8

import urllib2
import json
import time
import os

print("##### IPSWDownloader v0.7 #####")
print("##### Sviluppato da Dani Tox #####")

time.sleep(1.9)

urlAPI = "https://api.ipsw.me/v2.1/firmwares.json"
jsonOBJ = urllib2.urlopen(urlAPI)

data = json.load(jsonOBJ)

devicesIDs = data["devices"].keys()
devicesName = []

for key in devicesIDs:
    devicesName.append(data["devices"][key]["name"])

for index, name in enumerate(sorted(devicesName)):
    print(str(index) + ")\t" + name)

indexScelto = input("Scegli il numero che vuoi: ")

deviceNameScelto = sorted(devicesName)[indexScelto]
deviceIDScelto = ""

for deviceID in devicesIDs:
    if data["devices"][deviceID]["name"] == deviceNameScelto:
        deviceIDScelto = deviceID

print("Hai scelto: " + data["devices"][deviceIDScelto]["name"])
time.sleep(1)

deviceJson = data["devices"][deviceIDScelto]
deviceOSVersions = []

for index,firmware in enumerate(deviceJson["firmwares"]):
    deviceOSVersions.append(deviceJson["firmwares"][index]["version"])


for index, OSversion in enumerate(deviceOSVersions):
    print (str(index) + ")\t" + OSversion)

indexOSVersionScelto = input("Scegli l'OS che vuoi: ")
OSVersionScelto = deviceOSVersions[indexOSVersionScelto]

print("Hai scelto:\nVersione:\t" + deviceJson["firmwares"][indexOSVersionScelto]["version"])
print("È firmato?:\t" + "Si" if deviceJson["firmwares"][indexOSVersionScelto]["signed"] == True else "No")

time.sleep(2)

urlDownload = deviceJson["firmwares"][indexOSVersionScelto]["url"]

print("Inizio a scaricare...")
time.sleep(1)

os.chdir("/Users/danitox/Downloads")

os.system("wget " + urlDownload)
