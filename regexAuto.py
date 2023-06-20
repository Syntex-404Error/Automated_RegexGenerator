import re

def generate_regex_pattern(string):

 pattern =string

 result = ""

 if(len(string)==0):

  return result

 if pattern[0].isdigit():

  result+="\\d"

 elif pattern[0].isalpha():

  result+="[a-zA-Z]"

 else:

  result+=pattern[0]

 cnt=1

 for i in range(1,len(pattern)):

  num= pattern[i].isdigit()

  alph = pattern[i].isalpha()

  numpre= pattern[i-1].isdigit()

  alphpre= pattern[i-1].isalpha()

  if(numpre & num):

    cnt+=1

  elif(alphpre & alph):

    cnt+=1

  elif(alphpre == 1 and alph == 0):

    result+="{"+str(cnt)+"}"

    cnt=1

    if(num==1):

      result+="\\d"

    else:

      result+=pattern[i]

  elif(numpre==1 and num==0):

    result+="{"+str(cnt)+"}"

    cnt=1

    if(alph==1):

      result+="[a-zA-Z]"

    else:

      result+=pattern[i]

  elif(alphpre==0 and numpre==0):

    if(alph==1):

      result+="[a-zA-Z]"

    elif(num==1):

      result+="\\d"

    else:

      result+=pattern[i]

    cnt=1

 result+="{"+str(cnt)+"}"




#  print(result)

 return result