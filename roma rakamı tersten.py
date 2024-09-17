roma=input("1 ile 3999 arasında bir roma sayısı giriniz: ")
dizi=["I","V","X","L","C","D","M"]
dizi_kütüp={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
sayı=0
#roma=VII
for i in range(len(roma)-1):
    önceki= dizi.index(roma[i]) #2
    sonraki= dizi.index(roma[i+1]) #1
    if önceki<sonraki:
        sayı -= dizi_kütüp[roma[i]]
    else:
        sayı += dizi_kütüp[roma[i]]
sayı += dizi_kütüp[roma[-1]]    
print(sayı)   

