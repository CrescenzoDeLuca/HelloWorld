import math

cont=0
cont=int(cont)
print("inserire A --->")  
A=input()
A=int(A)
print("inserire B --->")
B=input()
B=int(B)
print("inserire C --->")
C=input()
C=int(C)

if A==0:
   cont=cont+2
if B==0:
   cont=cont+4
if C==0:
   cont=cont+8


if cont == 4:
   X1 = (C*-1)/A
   if X1 != 0:
      X2=X1*-1
      print("le soluzioni sono X=",X1," & X=",X2)

if cont == 8:
   X1=C
   X2=(B*-1)/A
   print("le soluzioni sono X=",X1," & X=",X2)

if cont == 10:
   X1 =0
   print("la soluzione è X=",X1)

if cont == 6:
   print("Non esiste X")

if cont == 12:
   X1 =0
   print("la soluzione è X=",X1)

if cont == 14:
   print("per ogni X")

if cont == 2:
   X1 = (C*-1)/B
   print("la soluzione è X=",X1)

else:
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



   