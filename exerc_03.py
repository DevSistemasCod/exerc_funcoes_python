
# Função para realizar a soma de dois números
def adicao(numero1,numero2):
    resultado = numero1 + numero2;
    return resultado

# Função para realizar a subtracao de dois números
def subtracao(numero1,numero2):
    resultado = numero1 - numero2;
    return resultado

# Função para realizar a multiplicacao de dois números
def multiplicacao(numero1,numero2):
    resultado = numero1 * numero2;
    return resultado

# Função para realizar a divisão de dois números
def divisao(numero1,numero2):
    if(numero2 == 0):
        print("Não existe divisão por zero !!!")
    else:
        resultado = numero1/numero2
        print("Resultado da Divisão: ",resultado)

# Função de Opções
def menu():
    opcao = 0
    while((opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4)):
        print("\n == Entre com o número da Operação Desejada ==")
        print(" 1 - Adição ")
        print(" 2 - Subtração ")
        print(" 3 - Multiplicação ")
        print(" 4 - Divisão \n")
        opcao = int(input("Informe a opção: "))

        if(opcao == 1):
            numero1 = float(input("Entre com o primeiro número: "))
            numero2 = float(input("Entre com o segundo número: "))
            resultado = adicao(numero1,numero2)
            print("Resultado da Adição: ", resultado)
    
        elif(opcao == 2):
            numero1 = float(input("Entre com o primeiro número: "))
            numero2 = float(input("Entre com o segundo número: "))
            resultado = subtracao(numero1,numero2)
            print("Resultado da Subtração: ",resultado)

        elif(opcao == 3):
            numero1 = float(input("Entre com o primeiro número: "))
            numero2 = float(input("Entre com o segundo número: "))
            resultado = multiplicacao(numero1,numero2)
            print(resultado)
            print("Resultado da Multiplicação: ",resultado)

        elif(opcao == 4):
            numero1 = float(input("Entre com o primeiro número: "))
            numero2 = float(input("Entre com o segundo número: "))
            divisao(numero1,numero2)

        else:
            print("Essa entrada não é aceita !!! \n")

# Função Principal
def main():
    menu()

if __name__ == "__main__":
    main()
