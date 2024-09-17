#ilk 30 Fibonacci sayısını bulup 1 karakter boşluk bırakarak yazdıran
#programı rekürsif olarak yazınız

#Fibonacci: 1 1  2   3   5   8
#           1 1 1+1 1+2 2+3 3+5

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

for i in range(30):
    print(fibonacci(i), end=" ")
    
#n=13 için 8'i ayırıp 5'i tekrar fibonacci olarak çağıracağız.
#yani fibonacci(8) + fibonacci(5)
#n=21 için 13'ü ayırıp 8'i tekrar fibonacci olarak çağıracağız
#yani fibonacci(13) + fibonacci(8)
              
