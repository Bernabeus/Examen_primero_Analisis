from pymongo import MongoClient
myClient = MongoClient ('mongodb://localhost:27017/')
try:
    myClient.admin.command('ismaster')
    print('MongoDB connection: Succes')
except ConnectionFailure as cf:
    print('MongoDB connection: Succes', cf)
    
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
import json
from bson.raw_bson import RawBSONDocument

    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))
response = requests.get('https://www.eluniverso.com/temas/juegos-olimpicos/')
soup = BeautifulSoup(response.content, "lxml")

Course=[]
Provider=[]
Duration=[]
Start_Date=[]
Offered_By=[]
No_Of_Reviews=[]
Rating=[]
Titulo=[]
Contenido=[]

post_titulo=soup.find_all("a", class_="no-underline")
post_contenido=soup.find_all("p", class_="summary | text-sm m-0 font-secondary")
extracted = []

for element in post_titulo:
    element=str(element)
    limpiar=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Titulo.append(limpiar.strip())
    
for element in post_contenido:
    element=str(element)
    limpiar=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Contenido.append(limpiar.strip())

#print(Titulo)
#print(Contenido)


archivo = pd.DataFrame({'titulo': Titulo})
archivo.to_json('tabla.json')
archivo = pd.DataFrame({'contenido':Contenido})
archivo.to_json('tabla1.json')

db = myClient["Examen"]
Collection= db["datosUniverso"]

with open('tabla.json') as file:
    file_data = json.load(file)

with open('tabla1.json') as file:
    file_data1 = json.load(file)
    
if isinstance (file_data, list):
    Collection.insert_many(file_data)
    Collection.insert_many(file_data1)
else:
    Collection.insert_one(file_data)    
    Collection.insert_one(file_data1)
