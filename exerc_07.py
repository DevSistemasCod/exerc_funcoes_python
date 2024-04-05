
# Função para convernter temperatura celsius em kelvin
def conveter_para_kelvin(temperatura_celsius):
     temperatura_kelvin = temperatura_celsius + 273
     return temperatura_kelvin

# Função para convernter temperatura celsius em fahrenheit
def conveter_para_fahrenheit(temperatura_celsius):
     temperatura_fahrenheit = ((1.8 * temperatura_celsius) + 32)
     return temperatura_fahrenheit

# Função menu para escolha do usuário
def menu():
    temperatura_celsius = float(input("Informe a temperatura em Celsius: "))
    opcao = 0

    while ((opcao != 1) and (opcao != 2)):
        print(" 1 - Converter em Kelvin")
        print(" 2 - Converter em Fahrenheit")
        opcao = int(input())

        if opcao == 1:
            temperatura_kelvin = conveter_para_kelvin(temperatura_celsius)
            print(f"Temperatura {temperatura_celsius} convertida em Kelvin: {temperatura_kelvin}")
        elif opcao == 2:
            temperatura_fahrenheit = conveter_para_fahrenheit(temperatura_celsius)
            print(f"Temperatura {temperatura_celsius} convertida em Fahrenheit: {temperatura_fahrenheit}")
        else:
            print("\n Opção Inválida !!!")

    

if __name__ == "__main__":
    menu()
