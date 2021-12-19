

def asal_sayı_mı(n):
     for i in range(2,n):
         #5 basamaklı n sayısının kendinden önceki sayılara bölünüp
         #bölünmediğini araştıracağız.
         if n%i!=0:
            continue
            #n, kendinden bir önceki sayıya bölünmüyorsa döngünün başına
            #geri dönüyoruz. Artık i değeri bir arttı.
         else:
             #n, i'ye tam bölünmüyorsa döngü burda kırılır ve for'un
             #hizasındaki else'i de okumaz.
            break
     else:
         #for döngüsü kırılmadan tamamlanmıştır. Şimdi alttaki kısım
         #okunacaktır.
         n=str(n)[0:-1]
         #sayının basamağı bir azaltılır.
         t=0 #dönüş sayısını ifade eder
         for m in range(len(n)):
             #n artık 4 basamaklı olduğundan baştaki fonksiyona geri döneriz
             #ve tekrar kontrol ederiz.
             t += 1
             return asal_sayı_mı(int(n))
            #asal olmadığında daha en başta döngüyü kırmıştık. Eğer döngü
            #basamak sayısı kadar dönebiliyorsa demek ki süper asaldır.
         if t==len(n):
             print(n,"süper asaldır")
     
         
n=int(input("Beş basamaklı bir sayı giriniz: "))
asal_sayı_mı(n)
