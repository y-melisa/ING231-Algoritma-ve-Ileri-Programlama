#Araya yerleştirme sıralama algoritması (insertion sort)
"""Soldan başlayarak elemanlar tutulur. İkinci eleman birinci eleman ile karşı..
laştırılır ve büyüklük sıralamasına göre yerleştirilir. Üçüncü eleman tutulur
ve soldakilerle karşılaştırılarak olması gereken yere yerleştirilir.Bu şekilde
sondan bir önceki eleman tutulana kadar devam eder."""
veri=[7,3,2,5,1,4] #len(veri)=6
for i in range(len(veri)):#0...5
    if i==0:
        continue      
    for m in range(i,0,-1):
        if veri[m]<veri[m-1]:
            if i!=1 and m != 0:
                liste=[]
                liste.extend(veri[:m-1])
                liste.append(veri[m])
                liste.append(veri[m-1])
                liste.extend(veri[m+1:])
                veri=liste
            elif i==1:
                liste=[]   
                liste.append(veri[m])
                liste.append(veri[m-1])
                liste.extend(veri[m+1:])
                veri=liste  
            print(liste)
    







