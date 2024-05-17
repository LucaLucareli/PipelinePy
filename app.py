from random import randint
from datetime import date

def is_positive(x):
    if (x > 0): 
        return x
    else: 
        numero = int(input("Digite um número inteiro positivo: ")) 
        if is_positive(numero):
            return numero

def is_pair_or_odd(x):
    if (x % 2 == 0):
        print ("Número par")
    else:
        print("Número impar")   

def validar_senha(senha):
    if(len(senha) < 8):
        return False
    maiuscula = False
    minuscula = False
    caracterExpecial = False
    for i in senha:
        if i.isupper():
            maiuscula = True
        if i.islower():
            minuscula = True
        if i == '!' or i == '#' or i == '@' or i == '$' or i == '%':    
            caracterExpecial = True
    if maiuscula == False or caracterExpecial == False or minuscula == False:
        return False
    return True



#Ex 1

# lado1 = int(input ("Digite o primeiro lado do triangulo: "))
# lado1 = is_positive(lado1)

# lado2 = int(input ("Digite o segundo lado do triangulo: "))
# lado2 = is_positive(lado2)

# lado3 = int(input ("Digite o terceiro lado do triangulo: "))
# lado3 = is_positive(lado3)

# if (lado1<(lado2+lado3) and lado2<(lado1+lado3) and lado3<(lado2+lado1)):
#     print("É um triangulo")
# else:
#     print("Não é um triangulo")



#Ex 2
# num = int(input("Digite um número para eu te contar se ele é par ou impar: "))
# num = is_positive(num)
# is_pair_or_odd(num)        
        

#Ex 3

# while True:
#     num_aleatorio = randint(1,10)

#     num_colocado  = int(input("Digite um número positivo e inteiro:  "))

#     if (num_aleatorio == num_colocado):
#         print("O número que você digitou é igual\nVocê ganhou")
#     else:
#         print("Você perdeu\nBoa sorte na proxima")    

#     escolha = int(input("Se não quiser jogar de novo digite 0, se quiser continuar pode colocar o que quiser:  "))

#     if (escolha == 0):
#         break   
        
# #Ex 4

# senha = input("Digite uma senha:   ")
# if validar_senha(senha):
#     print("Boa senha")
# else:
#      print("Senha não está de acordos com o padrão")    



#Ex 5 (desafio)
# carneL = ["File Duplo", "Alcatra", "Picanha"]
# fileAte = [4.9, 5.9, 6.9]
# fileAcima = [5.8, 6.8, 7.8]

# debito = ""
# quantPaga = 0
# totalDesconto = 0

# print("                                 Até 5 Kg                              Acima 5 Kg")
# print("[1] File Duplo   R$ ", fileAte[0], " por kg        R$ ", fileAcima[0]  , " por kg")
# print("[2] Alcatra      R$ ", fileAte[1], " por kg        R$ ", fileAcima[1]  , " por kg")
# print("[3] Picanha      R$ ", fileAte[2], " por kg        R$ ", fileAcima[2]  , " por kg")
# print("\nSó pode levar um tipo de carne\n\n")
# escolha = int(input("Digite o número para escolher a carne: "))
# quantidade = float(input("Dígite a quantidade( quantos kg ) que você quer: "))
# escolha = escolha -1

# if(quantidade > 5):
#     quantPaga = fileAcima[escolha]  * quantidade
# else:
#     quantPaga = fileAte[escolha] * quantidade

# formaPagamento = int(input("Forma de pagamento débito \n[1] SIM\n[2] NÂO\n --> "))
# if (formaPagamento == 1):
#     debito = "SIM"
#     totalDesconto = quantPaga * 0.95
# else:
#     debito = "NÃO"
#     totalDesconto = quantPaga

    

# print("Cupom fiscal: \nCarne: ", carneL[escolha] ,"\nQuantidade: ", quantidade ,"\nPreco: ", quantPaga ,"\nCartão de débito: ", debito ,"\nTotal com desconto: " ,totalDesconto)


# #Ex 5 (desafio)

# carneL = ["File Duplo", "Alcatra", "Picanha"]
# fileAte = [4.9, 5.9, 6.9]
# fileAcima = [5.8, 6.8, 7.8]

# debito = ""
# quantPaga = 0
# totalDesconto = 0

# print("                                 Até 5 Kg                              Acima 5 Kg")
# print("[1] File Duplo   R$ ", fileAte[0], " por kg        R$ ", fileAcima[0]  , " por kg")
# print("[2] Alcatra      R$ ", fileAte[1], " por kg        R$ ", fileAcima[1]  , " por kg")
# print("[3] Picanha      R$ ", fileAte[2], " por kg        R$ ", fileAcima[2]  , " por kg")
# print("\nSó pode levar um tipo de carne\n\n")
# escolha = int(input("Digite o número para escolher a carne: "))
# quantidade = float(input("Dígite a quantidade( quantos kg ) que você quer: "))
# escolha = escolha -1

# if(quantidade > 5):
#     quantPaga = fileAcima[escolha]  * quantidade
# else:
#     quantPaga = fileAte[escolha] * quantidade

# formaPagamento = int(input("Forma de pagamento débito \n[1] SIM\n[2] NÂO\n --> "))
# if (formaPagamento == 1):
#     debito = "SIM"
#     totalDesconto = quantPaga * 0.95
# else:
#     debito = "NÃO"
#     totalDesconto = quantPaga

    

# print("Cupom fiscal: \nCarne: ", carneL[escolha] ,"\nQuantidade: ", quantidade ,"\nPreco: ", quantPaga ,"\nCartão de débito: ", debito ,"\nTotal com desconto: " ,totalDesconto)


# def buscar_preco_prox(tupla, valor):
#     busca = tuple(abs(valor - tupla[i]) for i in range(len(tupla)))
#     return (busca.index(min(busca)), busca.index(max(busca)))

    
# tupla = (3.14, 2.718, 1.618) 
# valor = 10

# resultado = buscar_preco_prox(tupla,valor)
# if resultado[0] == resultado[1]:
#     print("Só tem um valor", resultado[0])
# else:
#     print(resultado)




