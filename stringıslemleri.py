import string

isimler = ["Ah5me4t" , "M9eHm4eT" ,"Ha3K5a1n"]
bosluk = "-"
def temizveri():
    str1 = isimler [0]
    str2 = isimler [1]
    str3 = isimler [2]
    
    
    
    str1 = ''.join((item for item in str1 if not item.isdigit()))
    
    str2 = ''.join((item for item in str2 if not item.isdigit()))
    
    str3 = ''.join((item for item in str3 if not item.isdigit()))
    
    
    print(str1.lower() +bosluk + str2.lower() +bosluk  + str3.lower())
      

temizveri()
    
