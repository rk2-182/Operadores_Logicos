#AND
#OR
#NOT


#Verdadero True = 1 False = 0

print("_________Operadores Logicos________")
print("AND")
#And Multiplicacion logica
print(True and True)    #1*1 = 1
print(True and False)   #1*0 = 0  
print(False and True)   #0*1 = 0   
print(False and False)  #0*0 = 0
print("OR")
#Or Suma logica
print(True or True)     #1+1 = >1
print(True and False)   #1+0 = 1
print(False and True)   #0+1 = 1
print(False and False)  #0+0 = 0
print("Not")
#Not Negacion
print(not(True))    #resultado: False
print(not(False))   #resultado: True

print("\n")
print("Prioridad de los operadores")
#Prioridad de los operadores logicos
#1. NOT
#2. AND
#3. OR

a=10
b=12
c=13
d=10

print("resutado")
print(((a>b) or (a<c)) and ((a==c) or (a>=b)))

#Prioridad de los operadores en general
"""
1. ()
2. **
3. *, /, mod, not
4. +,-, and
5.->,< ==, >=, <=, !=, or
"""




