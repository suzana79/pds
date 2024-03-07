import forca
import adivinhacao
def escolha_jogo():
        print("*************")
        print("**Escolha o jogo**")
        print("*************")
        print("(1) Forca (2) Adivinhação")
        jogo = int(input("Escolha o jogo"))
        if(jogo == 1):
            print("Jogando forca")
            forca.jogar_forca()
        elif(jogo == 2):
            print("Jogando adivinhacao")
            adivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolha_jogo()