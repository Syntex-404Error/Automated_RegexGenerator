

import gzip
import shutil

def convertoo(filenam):

# Specify the paths for the BSON.gz file and the output BSON file
 bson_gz_file = filenam
 bson_file = 'ooooolinkoutput.bson'

# Open the BSON.gz file in binary mode
 with gzip.open(bson_gz_file, 'rb') as gz_file:
    # Open the output BSON file in binary mode
    with open(bson_file, 'wb') as output_file:
        # Copy the contents from the gzipped file to the output BSON file
        shutil.copyfileobj(gz_file, output_file)

 print(f"Converted BSON to JSON. Output file: {bson_file}")

 return bson_file