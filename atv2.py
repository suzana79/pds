try:
    n1= float(input("digite um número")) 
    n2= float(input("digite um segundo número")) 
except ValueError: 
        print("tente novamente")
soma = n1+n2 
  
print (f"O número {n1} mais o número {n2} é igual a: {soma}.")
