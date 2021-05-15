

dosya = open ("odev.txt")


dosya = open("odev.txt","r")
for satir in dosya:
   satir = satir.replace('2','')
   satir = satir.replace('+','')
   satir = satir.replace('1','')
   satir = satir.replace('3','')
   satir = satir.replace('4','')
   satir = satir.replace('5','')
   satir = satir.replace('6','')
   satir = satir.replace('7','')
   satir = satir.replace('8','')
   satir = satir.replace('9','')
   satir = satir.replace('(','')
   satir = satir.replace(')','')
   satir = satir.replace('-','')
   satir = satir.replace('=','')
   satir = satir.replace('/','')
   satir = satir.replace('-','')
   satir = satir.replace('?','')
   print(satir)

print(satir)





