def ff(n):
    if n==1:
       return n
    else: 
        return n*ff(n-1)
    
num=int(input("Ievadi skaitli: "))

if num<0:
   print("Atvainojiet, no negatīva skaitļa nevar aprēķināt faktoriālu!")

elif num==0:
    print("Faktoriāls no nulles ir 1")

else:
    print(f'Skaitļa {num} faktoriāls ir {ff(num)}')