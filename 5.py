from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument
from pymongo.errors import ConnectionFailure
import sqlite3
recolectar = sqlite3.connect("examenbimes.db")

dato1 = pd.read_csv('C:/Users/Usuario/Desktop/Semestre 4/Analisis de datos/Node/TikTok/olimpicocol_1627692859660.csv', index_col=0)
dato2 = pd.read_csv('C:/Users/Usuario/Desktop/Semestre 4/Analisis de datos/Node/TikTok/olympicteamisrael_1627692706209.csv', index_col=0)

dato1.to_sql('olimpicocol', recolectar)
dato2.to_sql('olympicteamisrael', recolectar)
