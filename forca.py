import jogos  

def jogar_forca():
        palavra_secreta = "paraiso"
        letras_acertadas = ["_","_","_","_","_","_","_"]
        tentativas = 3 

        while tentativas > 0 and "_" in letras_acertadas:
            palpite = input("Digite uma letra:").lower()
            
            if palpite in palavra_secreta: 
                index = 0 
                for letra in palavra_secreta :
                    if palpite == letra :
                        letras_acertadas [index] = letra
                    index += 1 
            else : 
                tentativas -= 1
                print (f"Você tem {tentativas} tentativas.")
            
            print (" ".join(letras_acertadas))
                
        if "_" not in letras_acertadas : 
            print ("PARABÉNS VC GANHOU!!!")
        else :
            print (f"perdeu AAKAKAKAKAKKA. A palavra era:", palavra_secreta)
        jogos.escolha_jogo
            
if(__name__ == "__main__"):
        jogar_forca()