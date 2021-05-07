
sayi = int(input("Sayı giriniz:"))

asalmi = True

for x in range(2,sayi):
   if sayi%x==0:
    asalmi=False
    break

if asalmi==True:
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.")
    
