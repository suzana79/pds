import random

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    vitorias = 0
    print("Bem-vindo ao jogo Jokenpô!")
    print("Escolha: pedra, papel, tesoura.")

    while True: 
        escolha_jogador = input("Sua escolha:").lower()
        if escolha_jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue 

        escolha_computador = random.choice(opcoes)

        print(f"Computador escolheu: {escolha_computador}")

        resultado = define_ganhador(escolha_jogador, escolha_jogador)
        print (resultado)

        if resultado == "Você ganhou!":
            vitorias += 1
        elif resultado == "Você perdeu :(":
            vitorias -= 1
        else:
            vitorias += 0
        
        print (f"Total de vitórias: {vitorias}")

        jogar_novamente = input("Você quer jogar novamente?").lower()
        if jogar_novamente != "sim":
            break 
def define_ganhador(escolha_jogador, escolha_computador):
        if escolha_jogador == escolha_computador:
            return "Empate"
        elif (
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
            (escolha_jogador == "tesoura" and escolha_computador == "papel") 
            ):
            return "Você ganhou!"
            
        else : 
            return "Você perdeu :(" 


if __name__== "__main__":
    jogar_jokenpo()