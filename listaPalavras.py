try:
  listaPalavras = []
  quantPalavras = int(input("Digite a quantidade de palavras a serem analisadas: "))

  for i in range(quantPalavras):
      palavra = input(f"Digite a palavra {i + 1}: ")
      cont = {}
      repetidos = []
      naoRepete = []

      for letra in palavra:
          if letra in cont:
            cont[letra] += 1
          else:
            cont[letra] = 1

      for letra, quant in cont.items():
        if quant > 1:
          repetidos.append(f"'{letra}' se repete {quant} vezes")
        else:
          naoRepete.append(letra)

      print(f"\nResultados para a palavra:", palavra)
      print(f"Caracteres Repetidos:", ', '.join(repetidos))
      print(f"Caracteres Não Repetidos:", ', '.join(naoRepete))
      print()

except ValueError:
    print("Erro: Por favor, digite um número válido para a quantidade de palavras.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
