#yıgın yapısı, veri ekle ve veri çek metodlarını içermeli

def veri_ekle(veri):
    global liste
    liste.append(veri)
    print("yeni yığın:",liste)
    return baslangic()

def veri_çek(liste):
    print("çekilen veri: ",liste[-1])
    liste.pop()
    return baslangic()
    
def girilen(x):
    if x == "veri ekle":
        veri=input("Eklenecek bir veri giriniz: ")
        return veri_ekle(veri),veri

    elif x == "veri çek":
        if len(liste)==0:
            print("veri yoktur!")
        else:
            return veri_çek(liste)
    else:
        print("yanlış giriş yaptınız!")
        return baslangic()

def baslangic():
    x=input("veri eklemek için veri ekle, veri çekmek için veri çek yazınız: ")  
    girilen(x)

liste=[]   
baslangic()    

