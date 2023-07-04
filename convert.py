import pymongo
import bson
import re
# Specify the path to the BSON file
def bsonn(fileee):
 bson_file = fileee

# Open the BSON file in binary mode and read its contents
 with open(bson_file, 'rb') as file:
    # Parse the BSON data
    bson_data = bson.decode_all(file.read())
 pp=0

 t=[]


 for document in bson_data:

    for x in document:
    
        if x=='id':
         t.append(document[x])
         #print(document[x])
         #pp=pp+1
         break

 return t