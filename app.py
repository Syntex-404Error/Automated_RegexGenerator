from flask import Flask, request, render_template
from regexAuto import generate_regex_pattern
#from demo import import_dump_data
from convert import bsonn
from converter import convertoo
import re
import gzip
import json
from werkzeug.utils import secure_filename
from bson import decode_all
from bson.json_util import dumps
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/success', methods = ['POST','GET'])  
def success():  
  if request.method == 'POST':  
     file = request.files['file']
     file.save(file.filename)
     print(file.filename)
        # ttt=file.filename
    #newname=convertoo(file.filename)
        
        
        #lines=import_dump_data(file.filename)


     

# Connect to MongoDB
#  trial -----------------------------------------------

     client = MongoClient('mongodb://localhost:27017')

# Select the database and collection
     db = client.newdbb
     collection = db.newCollectionss

# Retrieve data from the collection
     datta = collection.find({}, {'id': 1})
    # for item in data:
    # # Access and use item['your_field_name'] or other fields as needed
    #  print(item)

#  trial -----------------------------------------------

     with open(file.filename, errors="ignore") as data:
        lines = data.readlines() #readlines

    #     # with open(file.filename,"r") as data:
    #     #     lines = data.readlines() #readlines

    #     #trial
    #     lines=bsonn(lines)
        #lines=bsonn(data)
    #lines=data
           
        
        #lines=bsonn(newname)

        # print(lines)




#         bson_file_path = 'C:/Users/HumanSharma/Downloads/file.filename'
# #compressed_data=[]
# # Open the compressed BSON file in binary mode
#         with gzip.open(bson_file_path, 'rb') as file:
#     # Read the compressed BSON data
#            lines = file.read()
#   #  decompressed_data = gzip.decompress(file.read())
# # Decompress the BSON data

# #print(type(decompressed_data))
#         print(len(lines))
# # Iterate over BSON documents

#         print(lines)

           
        #trial  

        #print(lines) check ok
       # print(len(lines))
        #cleaning of data
        new_list=[]
       # if file.filename
        if (file.filename).endswith('.txt'):
         t = []

         for l in lines:
            try:
             as_list = l.split(", ")
             t.append(as_list[0].replace("\n", ""))
            except:
               continue  

         cleaned_data = []

         for it in t:
            remove_space = it.strip()
            remove_comma = remove_space.replace(",","")
            n = len(remove_comma)
            remove_ann = remove_comma[1:n-1]
            cleaned_data.append(remove_ann)
         cleaned_data.sort()

       

        #new_list = set()
         for it in cleaned_data:
            if(len(it)==0):
                temp = it.strip()
                cleaned_data.remove(temp)




        #generating regex
        #cleaned_data=bsonn(cleaned_data)
        #print(cleaned_data)


        #print(len(cleaned_data)) #ok

        #print("bleh")

        #yaha se code h
        else:
         cleaned_data=lines 

        for it in cleaned_data:
            result=generate_regex_pattern(it)

            if(len(result)==0):
                continue

            result = "(" + result +  ")"
            if result not in new_list:
                new_list.append(result)
       
        ds = []
        xx = sorted(new_list, reverse=True)

        while xx:
           min = xx[0]  
           for x in xx: 
                if len(x) > len(min):
                 min = x
           ds.append(min)
           xx.remove(min)    

        print(ds)
        print(new_list)
        print("Successfully run")

        

        output_data=[]
        for X in ds:
          output_data.append({
                "regex_patterns": X
        })

        with open("regex_patterns.json", "w") as json_file:
         json.dump(output_data, json_file,indent=5)


        print("Regex patterns saved to regex_patterns.json")
        return render_template("result.html", ds = ds)




    #   return render_template("result.html", new_list = ds)

   

   




@app.route("/res")

def display():

    return render_template('result.html')

if __name__ == "__main__":

    app.run(debug=True)