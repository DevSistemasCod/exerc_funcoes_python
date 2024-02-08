
#Método para invernter uma string
def inverter_string(palavra):
    string_invertida = ""

    for i in palavra:
        print(i)
        #construção da string invertida
        string_invertida = i + string_invertida
    return string_invertida


def main():
    palavra = input("Digite uma string: ")
    string_invertida = inverter_string(palavra)
    print(f"A string invertida é: {string_invertida}")

if __name__ == "__main__":
    main()