atletas = []
quant = int(input("insira quantos atletas deseja inserir: "))

for i in range(quant):
    nome = input("Nome: ")
    saltos = []
    for i in range(3):
            while True:
                try:
                    dist = float(input(f"Digite a distância do salto {i + 1}: "))
                    break
                except ValueError:
                    print("Por favor, digite um número válido.")
            saltos.append(dist)
    atleta = {"nome": nome, "saltos": saltos}
    atletas.append(atleta)
    print("Atleta cadastrado com sucesso!")

while True:
    print("\nMenu:")
    print("1 - Visualizar todos os atletas")
    print("2 - Visualizar atleta com maior média de salto")
    print("3 - Visualizar atleta com maior salto")
    print("4 - Modificar o salto de um atleta")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("\nLista de atletas cadastrados:")
        for atleta in atletas:
            print(f"Nome: {atleta['nome']}, Saltos: {atleta['saltos']}")

    elif opcao == "2":
            melhorMed = 0
            nomeMelhMed = ""
            for atleta in atletas:
                media = sum(atleta['saltos']) / 3
                if media > melhorMed:
                    melhorMed = media
                    nomeMelhMed = atleta['nome']
            print(f"Atleta com a maior média de salto: {nomeMelhMed}, Média: {melhorMed:.2f}")

    elif opcao == "3":
            maiorSalto = 0
            nomeMaiorSalto = ""
            for atleta in atletas:
                maior = max(atleta['saltos'])
                if maior > maiorSalto:
                    maiorSalto = maior
                    nomeMaiorSalto = atleta['nome']
            print(f"Atleta com o maior salto: {nomeMaiorSalto}, Maior salto: {maiorSalto}")

    elif opcao == "4":
        nomeNovo = input("Digite o nome do atleta que deseja modificar o salto: ")
        encontrado = False
        for atleta in atletas:
            if atleta['nome'] == nomeNovo:
                for i in range(3):
                    while True:
                        try:
                            novaDist = float(input(f"Digite o novo valor para o salto {i + 1}: "))
                            atleta['saltos'][i] = novaDist
                            encontrado = True
                            break
                        except ValueError:
                            print("Por favor, digite um número válido.")
                print("Salto modificado com sucesso!")
                break
        if not encontrado:
            print(f"Atleta {nomeNovo} não encontrado.")

    elif opcao == "5":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
