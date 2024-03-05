    import random
    def jogar():
        numero_secreto = random.randint(1,10)
        tentativas = 1
        max_tentativas = 5
        
        while tentativas < max_tentativas :
            palpite = int(input("digite o seu palpite"))
            tentativas += 1
            if palpite == numero_secreto:
                print (f"parabéns, você acertou")
                break 
            elif palpite > numero_secreto:
                print (f"tente um  numero menor")
            else :
                print(f"tente um número maior")
                
            if tentativas < max_tentativas:
                print (f"você tem {max_tentativas - tentativas} tentativas")
            else:
                print(f"você não acertou o número era {numero_secreto}")
                
        print("Fim de jogo")

 if(__name__ == "__main__"):
            jogar()   
        