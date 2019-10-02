import wget
import pandas as pd
import os

LutronData = pd.read_csv("Lutron SpecSheet CAD RVT.csv") 
PanasonicData = pd.read_csv("Complete Panasonic Spec Sheet HxWxD W.csv") 
ONQdata = pd.read_csv("Complete ON-Q Spec Sheet HxWxD URL.csv") 
path = os.getcwd()


print("Lutron")
try:
    os.makedirs(f"{path}\Lutron\Spec")
except FileExistsError:
    print('file already exists')
for model in LutronData.loc[:,"index"]:
    url = LutronData.loc[model,"specURL"]
    try:
        wget.download(url, f"{path}\Lutron\Spec\{LutronData.loc[model,'Model Number']}.pdf")
        print(f"{LutronData.loc[model,'Model Number']}  is downloaded!")
    except AttributeError:
        print(f"{LutronData.loc[model,'Model Number']}  does not have a Spec Sheet!")
 
print("Panasonic")       
try:
    os.makedirs(f"{path}\Panasonic\Spec")
except FileExistsError:
    print('file already exists')
for model in PanasonicData.loc[:,"index"]:
    url = PanasonicData.loc[model,"URL"]
    try:
        wget.download(url, f"{path}\Panasonic\Spec\{PanasonicData.loc[model,'Model Number']}.pdf")
        print(f"{PanasonicData.loc[model,'Model Number']}  is downloaded!")
    except AttributeError:
        print(f"{PanasonicData.loc[model,'Model Number']}  does not have a Spec Sheet!")
               
print("ON-Q")       
try:
    os.makedirs(f"{path}\ON-Q\Spec")
except FileExistsError:
    print('file already exists')
for model in ONQdata.loc[:,"index"]:
    url = ONQdata.loc[model,"URL"]
    try:
        wget.download(url, f"{path}\ON-Q\Spec\{ONQdata.loc[model,'Model Number']}.pdf")
        print(f"{ONQdata.loc[model,'Model Number']}  is downloaded!")
    except AttributeError:
        print(f"{ONQdata.loc[model,'Model Number']}  does not have a Spec Sheet!")

#url = "https://www.python.org/static/img/python-logo@2x.png"
#wget.download(url, 'c:/users/LikeGeeks/downloads/pythonLogo.png')
#LutronData.loc["Row","Col"]
#os.mkdir(f"{path}\Lutron")
