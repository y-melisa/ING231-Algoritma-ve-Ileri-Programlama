import random
def random_tut():
    global a
    a=random.randint(1000,10000)
    a=str(a)
    if a[0]!=a[1] and a[0]!=a[2] and a[0]!=a[3] and a[1]!=a[2] and a[1]!=a[3] and a[2]!=a[3]:
      
        return girilen_sayı()
    else:
        return random_tut()

def girilen_sayı():
    b=input("4 basamaklı rakamları farklı bir sayı giriniz: ")
    if len(b)!=4 or b[0]=="0":
        print("4 basamaklı bir sayı girmediniz!")
        return girilen_sayı()
    if b[0]!=b[1] and b[0]!=b[2] and b[0]!=b[3] and b[1]!=b[2] and b[1]!=b[3] and b[2]!=b[3]:
        doğru_yer = 0
        yanlış_yer = 0
        if a==b:
            print("Doğru tahmin ettiniz!")
        else:
            for i in range(len(a)): #8506   #i=0,1,2,3
                for k in range(len(b)): #8512  k=0,1,2,3
                    if i==k: #0==0
                        if b[k]==a[i]:
                            doğru_yer= doğru_yer + 1
                    elif b[k]==a[i]:
                        yanlış_yer = yanlış_yer - 1
                    else:
                        continue
            print("Doğru yer sayacı: ",doğru_yer,"Yanlış yer sayacı: ",yanlış_yer)
            
            return girilen_sayı()
        
    else:
        print("Rakamları farklı bir sayı girmediniz!")
        return girilen_sayı()
    
    
        
random_tut()
