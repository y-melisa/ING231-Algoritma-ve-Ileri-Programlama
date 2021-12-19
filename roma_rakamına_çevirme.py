#sadeleştirme
sayı=input("1 ile 3999 arasında bir sayı girin: ")
roma=""
uzunluk=len(sayı)
if uzunluk==4:
    roma += "M"*int(sayı[0])
if uzunluk==3 or uzunluk==4:
    if sayı[-3]<="3":
        roma += "C"*int(sayı[-3])
    elif sayı[-3]=="4":
        roma += "C" + "D"     
    elif sayı[-3]>="5" and sayı[-3]<="8":
        roma += "D" + "C"*(int(sayı[-3])%5)
    else:
        roma += "C"+"M"
if uzunluk==2 or uzunluk==3 or uzunluk==4:
    if sayı[-2]<="3":
        roma += "X"*(int(sayı[-2]))
    elif sayı[-2]=="4":
        roma += "X" + "L"
    elif sayı[-2]>="5" and sayı[-2]<="8":
        roma += "L"+"X"*(int(sayı[-2])%5)
    else:
        roma += "X"+"C"
if uzunluk==1 or uzunluk==2 or uzunluk==3 or uzunluk==4:
    if sayı[-1]<="3":
        roma += "I"*(int(sayı[-1]))
    elif sayı[-1]=="4":
        roma += "I" + "V"
    elif sayı[-1]>="5" and sayı[-1]<="8":
        roma += "V"+"I"*(int(sayı[-1])%5)
    else:
        roma += "I"+"X"

print(roma)
