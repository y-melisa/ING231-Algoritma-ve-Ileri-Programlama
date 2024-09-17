"""Başlarken dizinin ilk öğesini en küçük öğe kabul eder. Tabii, bu kabul
geçicidir. Sonra kalan terimler arasında daha küçükler varsa, onların en küçüğü
olan terimle takas eder. O terimi en sola koyar; bu terim sıralama sonunda ilk
terim olacaktır.Diziden seçilen bu en küçük terimi çıkarınca, geri kalan alt
dizine aynı yöntemi uygular. Altdiziden seçtiği en küçük öğeyi, ilk seçtiğinin
sağına koyar. Dizinin sol ucunda iki terimli alt dizi küçükten büyüğe doğru
sıralı bir altdizi oluşturur. Bu işleme kalan altdizinler bitene kadar devam
edilir. Her adım başlarken, sol yanda sıralı bir altdizi, sağ yanda sırasız bir
alt dizi vardır. Her adımda sıralı dizi bir terim artar, sırasız dizi bir terim
azalır. Sağ yandaki sırasız altdizi bitince, sıralama işlemi biter"""
veri=[43,44,6,0,2,23,9]

liste=[]

def mini_bulucu(veri):
    mini=veri[0]
    for m in range(1,len(veri)):#0,1,2,3,4,5
        if veri[m]<mini:
            mini=veri[m]
    return yeni_liste(mini)
    

def yeni_liste(mini):
    liste.append(mini)
    print("yeni sıra: ",liste)
    veri.pop(veri.index(mini))
    print("minimum aranacak yeni liste:",veri)
    while len(liste)!=7:
        return mini_bulucu(veri)
    


mini_bulucu(veri)


