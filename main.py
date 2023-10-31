import mysql.connector
import json

file = open('config.json', 'r')
configData = json.load(file)

sqlClient = mysql.connector.connect(  
    host=configData['host'],
    user=configData['user'],
    password=configData['pass']
)