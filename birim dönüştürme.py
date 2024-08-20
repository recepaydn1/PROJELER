print("BİRİM DÖNÜŞTÜRÜCÜYE HOŞGELDİNİZ")

print("1.KİLOMETRE")
print("2.METRE")
print("3.DESİMETRE")
print("4.SANTİMETRE")
print("5.MİLİMETRE")


işlem = (input("İLK BİRİMİ SEÇİNİZ 1,2,3,4,5,6:  "))
işlem2 = (input("İKİNCİ BİRİMİ SEÇİNİZ 1,2,3,4,5,6:  "))

ilkbirim = int(input("SAYIYI YAZINIZ:  "))

if işlem == "1" and işlem2 == "2":
 print(ilkbirim,"KİLOMETRE",ilkbirim*1000,"METREDİR")
 

if işlem == "1" and işlem2 == "3":
 print(ilkbirim,"KİLOMETRE",ilkbirim*10000,"DESİMETREDİR")
 
 
 
if işlem == "1" and işlem2 == "4":
  print(ilkbirim,"KİLOMETRE",ilkbirim*100000,"SANTİMETRE")



if işlem == "1" and işlem2 == "5":
  print(ilkbirim,"KİLOMETRE",ilkbirim*1000000 ,"MİLİMETRE")
 
################################################################################## KİLOMETRE

if işlem == "2" and işlem2 == "1":
 print (ilkbirim,"METRE",ilkbirim*0.001,"KİLOMETREDİR")


if işlem == "2" and işlem2 == "3":
 print(ilkbirim,"METRE",ilkbirim*10,"DESİMETREDİR")

 
 
if işlem == "2" and işlem2 == "4":
  print(ilkbirim,"METRE",ilkbirim*100,"SANTİMETRE")
  


if işlem == "2" and işlem2 == "5":
  print(ilkbirim,"METRE",ilkbirim*1000 ,"MİLİMETRE")
 
  ######################################################################################  METRE

if işlem == "3" and işlem2 == "1":
 print (ilkbirim,"DESİMETRE",ilkbirim*0.0001,"KİLOMETREDİR")


if işlem == "3" and işlem2 == "2":
 print(ilkbirim,"DESİMETRE",ilkbirim*0.1,"METREDİR")
 
 
 
if işlem == "3" and işlem2 == "4":
  print(ilkbirim,"DESİMETRE",ilkbirim*10,"SANTİMETRE")
  


if işlem == "3" and işlem2 == "5":
  print(ilkbirim,"DESİMETRE",ilkbirim*100 ,"MİLİMETRE")
  

#############################################################################      DESİMETRE

if işlem == "4" and işlem2 == "1":
 print (ilkbirim,"SANTİMETRE",ilkbirim*0.00001,"KİLOMETREDİR")
 

if işlem == "4" and işlem2 == "2":
 print(ilkbirim,"SANTİMETRE",ilkbirim*0.01,"METREDİR")
 
 
 
if işlem == "4" and işlem2 == "3":
  print(ilkbirim,"SANTİMETRE",ilkbirim*0.1,"DESİMETREDİR")
  


if işlem == "4" and işlem2 == "5":
  print(ilkbirim,"SANTİMETRE",ilkbirim*10 ,"MİLİMETREDİR")
  

##############################################################################    SANTİMETRE

if işlem == "5" and işlem2 == "1":
 print (ilkbirim,"MİLİMETRE",ilkbirim/1609344,"KİLOMETREDİR")
 

if işlem == "5" and işlem2 == "2":
 print(ilkbirim,"MİLİMETRE",ilkbirim/1000.0,"METREDİR")
 
 
 
if işlem == "5" and işlem2 == "3":
  print(ilkbirim,"MİLİMETRE",ilkbirim/100,"DESİMETREDİR")
 


if işlem == "5" and işlem2 == "4":
  print(ilkbirim,"MİLİMETRE",ilkbirim/10 ,"SANTİMETRE")
  

###############################################################################    MİLİMETRe