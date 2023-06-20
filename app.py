from flask import Flask, request, render_template
from regexAuto import generate_regex_pattern
import re
import json
from werkzeug.utils import secure_filename

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

        # file_content = file.read().decode('utf-8')
        # print(file_content)
        #file = open(test,"r")
        #filecontent = file.readlines()



        with open(file.filename,"r") as data:
            lines = data.readlines() #readlines

           

        #print(lines) check ok
        print(len(lines))
        #cleaning of data

        t = []

        for l in lines:
            as_list = l.split(", ")
            t.append(as_list[0].replace("\n", ""))  

        cleaned_data = []

        for it in t:
            remove_space = it.strip()
            remove_comma = remove_space.replace(",","")
            n = len(remove_comma)
            remove_ann = remove_comma[1:n-1]
            cleaned_data.append(remove_ann)
        cleaned_data.sort()

        new_list=[]

        #new_list = set()
        for it in cleaned_data:
            if(len(it)==0):
                temp = it.strip()
                cleaned_data.remove(temp)




        #generating regex

        #print(cleaned_data)

        #print(len(cleaned_data)) #ok

        #print("bleh")

        for it in cleaned_data:
            result=generate_regex_pattern(it)

            if(len(result)==0):
                continue

            result = "(" + result +  ")"
            if result not in new_list:
                new_list.append(result)
       
        ds = []

        while new_list:
           min = new_list[0]  
           for x in new_list: 
                if len(x) > len(min):
                 min = x
           ds.append(min)
           new_list.remove(min)    

        print(ds)
        print(new_list)
        print("khalli h")

        output_data=[]
        for X in ds:
          output_data.append({
                "regex_patterns": X
        })

        with open("regex_patterns.json", "w") as json_file:
         json.dump(output_data, json_file,indent=5)


        print("Regex patterns saved to regex_patterns.json")
        return render_template("result.html", ds = ds)




       # return render_template("result.html", new_list = ds)

   

   




@app.route("/res")

def display():

    return render_template('result.html')

if __name__ == "__main__":

    app.run(debug=True)