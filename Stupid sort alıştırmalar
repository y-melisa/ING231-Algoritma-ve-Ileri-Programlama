"""Saçma sıralama veya rastgele sıralama, bilgisayar bilimlerinde yalnızca
eğitim amaçlı olarak kullanılan verimsiz bir sıralama algoritması.
Bir deste oyun kağıdı saçma sıralama algoritmasıyla sıralanmak istendiğinde,
destenin sıralı olup olmadığına bakılır, eğer deste sıralı değilse havaya
atılarak yere düşen kartlar toplanarak deste yeniden oluşturulur. Bu işlem
deste sıralanana kadar sürer."""
import random
liste=[]
def oyun(veri):
    for i in range(len(veri)-1):
        if veri[i+1]>veri[i]:
            continue
        else: 
            for i in range(len(veri)):
                rastgele_veri=random.choice(veri)
                liste.append(rastgele_veri)
                veri.pop(veri.index(rastgele_veri))
            print(liste)
            return oyun(liste)
    print(liste)

veri=[32,43,6,10,20] #len=8
oyun(veri)

                       
        
        
        
        
