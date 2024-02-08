

def contar_digitos(numero):
    qtd_digitos = len(str(numero))
    return qtd_digitos

def main():
    numero = int(input("Informe o número: "))
    qtd_digitos = contar_digitos(numero)
    print(f"Quantidade de digitos: {qtd_digitos}")

if __name__ == "__main__":
    main()