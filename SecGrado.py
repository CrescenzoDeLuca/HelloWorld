import math


print("inserire A --->")
A=input()
A=int(A)
print("inserire B --->")
B=input()
B=int(B)
print("inserire C --->")
C=input()
C=int(C)

if A == 0 and B != 0 and C != 0:
   X1 = (C*-1)/B
   print("la soluzione è X=",X1)


if A != 0 and B == 0 and C != 0:
   X1 = (C*-1)/A
   if X1 != 0:
      X2=X1*-1
      print("le soluzioni sono X=",X1," & X=",X2)

if A !=0 and B!=0 and C == 0:
   X1=C
   X2=(B*-1)/A
   print("le soluzioni sono X=",X1," & X=",X2)

if A == 0 and B != 0 and C == 0:
   X1 =0
   print("la soluzione è X=",X1)

if A == 0 and B == 0 and C != 0:
   print("Non esiste X")

if A != 0 and B == 0 and C == 0:
   X1 =0
   print("la soluzione è X=",X1)

D1=(B**2)
D2=4*(A*C)
D=D1-D2
D=int(D)

if D > 0:
   S=math.sqrt(D)
   S=float(S)
   X1=(-B+S)/(2*A)
   X2=(-B+S)/(2*A)
   print("soluzioni X1=",X1," & X2=",X2)
if D == 0:
   X1=-B/(2*A)
   print("soluzione X=",X1)
if D < 0:
   print("non esiste X")



   