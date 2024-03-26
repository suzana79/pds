def lista():
    lista = []
    
def gravar_lista(lista):
    nome_arq = input("Digite o nome do arquivo.")
    with open(nome_arq,"w") as arquivo:
        for item in lista:
            arquivo.write(item+"\n")
    print(f"Arquivo gravado com sucesso!", nome_arq)
    while True:
        print("1 - Inserir novo item")
        print("2 - Excluir item")
        print("3 - Mostrar lista atual")
        print("4 - Gravar lista")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            novo_item = input("Digite o novo item: ")
            lista.append(novo_item)
            print("Item adicionado à lista!")
        
        elif opcao == "2":
            if lista:
                print("Lista atual:", lista)
                item_excluir = input("Digite o número do item que deseja excluir: ")
                if item_excluir.isdigit() and int(item_excluir) <= len(lista):
                    del lista[int(item_excluir)-1]
                    print("Item excluído!")
                else:
                    print("Opção inválida!")
            else:
                print("A lista está vazia!")
        
        elif opcao == "3":
            print("Lista atual:", lista)
        elif opcao == "4":
            ()
            nome_arq = input("Digite o nome do arquivo.")
        
        elif opcao == "5":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__== "__main__":
   lista()