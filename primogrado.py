a=input("inserisci a ")
a=int(a)
b=input("inserisci b ")
b=int(b)
if a==0 and b==0:
   print("per ogni X")
elif a==0:
   print("X non esiste")
else:
    b=-b
    x=b/a
    print(x)