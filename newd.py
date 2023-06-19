import re
import json

regex_patternssss=set()
# Step 1: Define the input patterns
input_patterns = [
"E-00000-AA-6180-00050",
"E-00000-AA-6180-00051",
"E-00000-AA-6180-00052",
"E-00000-AA-6180-00053",
# "E-00000-AA-6180-00054",
# "E-00000-AA-6180-00055",
# "E-00000-AA-6180-00056",
# "E-00000-AA-6180-00057",
# "E-00000-AA-6180-00058",
# "E-00000-AA-6180-00059",
# "E-00000-AA-6180-00060",
# "E-00000-AA-6180-00061",
# "E-00000-AA-6180-00062",
# "E-00000-AA-6180-00063",
# "E-00000-AA-6180-00064",
# "E-00000-AA-6180-00065",
# "E-00000-AA-6180-00066",
# "E-00000-AA-6180-00067",
# "E-00000-AA-6180-00068",
# "E-00000-AA-6180-00069",
# "1\"-A88127-11001-N",
# "\"-A88128-11001-N",
# "\"-A88129-11001-N",
# "\"-A88133-11001-N",
# "1\"-A88134-11001-N",
# "000LP1LP1",
# "000LP1LP1",
# "000LP1LP1",
# "000LP1LP1",
# "000LP1LP1",
# "000HS-204-SHS-204-S",
# "000HS-204-SHS-204-S",
# "000HS-204-SHS-204-S",
# "000HS-204-SHS-204-S",
# "000HS-204-SHS-204-S",
# "000HS-204-SHS-204-S",
# "000BC2BC2",
# "000BC2BC2",
# "000BC2BC2",
# "000BC2BC2",
# "000GAS1GAS1",
# "000GAS1GAS1",
# "000GAS1GAS1",
# "000GAS1GAS1",
# "000GAS1GAS1",
# "000GAS1GAS1",
# "000-MVY-105",
# "000-MVY-106",
# "000-MVY-106",
# "000-NRV-008",
# "000-NRV-008",
# "000-NRV-008",
# "000SA10",
# "000SAS10L1",
"000SAS10R1",
"000SB10",
# "000SD30",
# "E-00400-LF-2347-0001",
# "E-00400-LF-2347-0002",
# "E-00400-LF-2347-0003",
# "E-00000-LF-6023-0003",
# "A048-E-00000-AA-0702-0001",
# "A048-E-00000-AA-7180-0001",
# "A048-E-00000-CA-6180-0010",
# "A048-E-00000-CA-6180-0011",
# "A048-E-00000-CA-6180-0012",
"A048-E-00000-CA-6180-0013",
"A048-E-00000-CA-6180-0014",
# "04-AK0001",
# "23-AG1002",
# "28-AS1003",
# "28-AS1004",
# "A048-E-00000-AA-3347-0001"
]

# Step 2: Generate regex patterns
# regex_patternssss = []
# for pattern in input_patterns:
# # Perform any necessary transformations or manipulations on the input pattern
# # Generate the regex pattern using regular expressions
# processed_pattern = re.escape(pattern)  # Escape special characters
#     regex_pattern = re.sub(r"\\(.)", r"\1", processed_pattern)  # Remove escape characters


#regex_patternssss = []
for pattern in input_patterns:
#    # pattern = re.escape(data)  # Escape special characters in the data
#     #(\E)-([0-9]{5})-([A-Z]{2})-([0-9]{4})-([0-9]*\)
#     pattern = data.replace(r"E-00000-AA-6180-00050", r"(\E-[0-9]{5}-[A-Z]{2}-[0-9]{4}-[0-9]*\)")  # Replace spaces with a character class matching any letter
#    # pattern = pattern.replace(r"\d*", r"\d{5}")  # Replace consecutive digits with a fixed number of digits (e.g., "00000")
#     regex_patternssss.append(pattern)
  
# #regex_pattern= r"^\"?-?E-\d{5}-AA-6180-\d{5}\"?$"
 
 
 
#     # regex_patternssss.append(regex_pattern)
     regex_pattern =[
     r'[a-zA-Z]*',
     r'[0-9]*',
     r'\.?\-?',
     r'\.?\-?.?[a-zA-Z0-9]*\.?\-?.?',]
#     # regex_patternssss.append(regex_pattern)

# # Step 3: Save regex patterns to JSON file
# output_data = {
#     "regex_patterns": regex_patternssss
# }

# with open("regex_patternssss.json", "w") as json_file:
#     json.dump(output_data, json_file)





     string=''
    # escaped_pattern = re.escape(pattern)
     #escaped_pattern=pattern
     print(pattern)
     arr=re.split("(\d+)",pattern)
     #arr=re.split('(\d+)',pattern)
    #  arr=[]

    #  ar=re.match('([a-z]+)([0-9]+)(\-)',pattern,re.I)
    #  if ar :
    #   arr=ar.groups()
     
     print(arr)
     for x in arr:
       print(x)
       if(x.isdigit()):
           string=string+regex_pattern[1]
       elif(x.isalpha() ):   
           string=string+regex_pattern[0]
       elif(bool(re.match(regex_pattern[2],x))==True and x.__sizeof__()==1):
           string=string+regex_pattern[2]
       elif(bool(re.match(regex_pattern[3],x))==True ):
           string=string+regex_pattern[3]
     
           
     regex_patternssss.add(string)
          
     # print(arr[1])
    # Replace escaped digits with "\d" to match any digit
# regex_pattern = re.sub(r"\\E\\-\\00000", r"E-[0-9]*", escaped_pattern)
    
#     # Replace escaped quotation marks with "\" to match a quotation mark
# regex_pattern = re.sub(r"\\\"", r"\"",regex_pattern)
    
#     # Replace escaped spaces with "\s" to match any whitespace character
# regex_pattern = re.sub(r"\\ ", r"\\s", regex_pattern)
    
#regex_patternssss.append(regex_pattern)


# Step 3: Save regex patterns to a JSON file
output_data=[]
# for x in regex_patternssss:
#     output_data = {
#     "regex_patterns": x
# }
    
    # Step 3: Save regex patterns to JSON file
for x in regex_patternssss:
             output_data.append({
                "regex_patterns": x
        })

# with open("regex_patterns.json", "w") as file:
#     json.dump(output_data, file, ind)


with open("regex_patterns.json", "w") as json_file:
    json.dump(output_data, json_file,indent=5)



print("Regex patterns saved to regex_patterns.json")




