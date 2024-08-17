print("HESAP MAKİNESİNE HOŞGELDİNİZ")

print("1.TOPLAMA")
print("2.ÇIKARMA")
print("3.ÇARPMA")
print("4.BÖLME")

islem = input(print("İŞLEMİNİZİ SEÇİN:"
              "1","2","3","4"))

ilksayi = int(input("İLK SAYIYI GİRİNİZ: "))

ikincisayi = int(input("İKİNCİ SAYIYI GİRİNİZ: "))


if islem == "1":
    print("TOPLAMA İŞLEMİ YAPILACAKTIR")
    print("SONUÇ:", ilksayi+ikincisayi)

elif islem == "2":
    print("ÇIKARMA İŞLEMİ YAPILACAKTIR")
    print("SONUÇ:", ilksayi-ikincisayi)

elif islem == "3":
    print("ÇARPMA İŞLEMİ YAPILACAKTIR")
    print("SONUÇ:", ilksayi*ikincisayi)

if islem =="4":
    ikincisayi == 0
    print("HATA!! SIFIRA BÖLÜNMEZ")
else:
    print("BÖLME İŞLEMİ YAPILACAKTIR")
    print("SONUÇ: ", ilksayi/ikincisayi)



