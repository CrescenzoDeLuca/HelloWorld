import math

print("inserire Ax2 --->")  
A=input()
A=int(A)
print("inserire Bx --->")
B=input()
B=int(B)
print("inserire C --->")
C=input()
C=int(C)



if A==0 and B==0 and C==0:
         print("per ogni X")
elif A==0 and B==0:
   print("Non esiste X")
elif A==0:
    R=-C 
    R=C/B
    print(R)
else:
   D1=(B**2)
   D2=4*(A*C)
   D=D1-D2

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



   