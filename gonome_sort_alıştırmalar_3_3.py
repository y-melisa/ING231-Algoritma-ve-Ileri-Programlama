#Gonome sort (Cüce algoritması)
"""İlk elemanı seçer sonrakiyle karşılaştırır (küçük veya büyüğe) sıralamaya göre yer değiştirir.
Sonra ondan önceki eleman varsa bir öncekiyle karşılaştırır. Yer değiştirmezse tekrar kaldığı
elemandan aynı şekilde devam eder."""

veri=[5,3,1,200,10,7,0,-3,]   
print(veri)
for i in range(len(veri)): 
    for k in range(i):  
        if veri[i-k-1] > veri[i-k]: 
            önceki=veri[i-k-1]    
            sonraki=veri[i-k]       
            veri[i-k-1]=sonraki   
            veri[i-k]=önceki        
            print(veri)
        else:
            print(veri)
        
    
        
        
    