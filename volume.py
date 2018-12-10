import math
print (" vuoi calcolare il volume di una sfera -->1")
print (" vuoi calcolare il volume di un cubo -->2")
a=input()
a=int(a)
if a==1:
        r=input("inserisci raggio == ")
        r=int(r)
        volume=(4.0/3.0) * math.pi * r**3
        print("il volume e' ",volume)
elif a==2:
        l=input("inserisci lato")
        l=int(l)
        l=l**3
        print("in cubo e' ",l)