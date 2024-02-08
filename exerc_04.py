
# Contar Vogais
def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0

    # itera na string palavra 
    for i in palavra:
        # verifica se encontra alguma das vogais na string palavra
        if i in vogais:
            contador = contador + 1
    
    return contador

# função principal
def main():
    palavra = input("Informe uma palavra: ")
    quantidade_vogais = contar_vogais(palavra)
    print(f" Quantidade Vogais: ",quantidade_vogais)

if __name__ == "__main__":
    main()