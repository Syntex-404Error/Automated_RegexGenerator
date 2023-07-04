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


     client = MongoClient('mongodb://localhost:27017')

# Select the database and collection
     db = client.newdbb
     collection = db.newCollectionss

# Retrieve data from the collection
     datta = collection.find({}, {'id': 1})

    

#  trial -----------------------------------------------

     with open(file.filename, errors="ignore") as data:
        lines = data.readlines() #readlines

        lines=bsonn(file.filename)

        
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

       
         for it in cleaned_data:
            if(len(it)==0):
                temp = it.strip()
                cleaned_data.remove(temp)


        else:
         #print(lines)
         cleaned_data=[]
         for item in datta:
    # Access and use item['your_field_name'] or other fields as needed
           for x in item:
          #print(item)

             if x=='id':
         
              cleaned_data.append(item[x])
         #print(cleaned_data)

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