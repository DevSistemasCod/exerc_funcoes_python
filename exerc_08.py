#constantes globais
VALOR_DOLAR_EM_REAL = 4.96
VALOR_EURO_EM_REAL = 5.34
VALOR_LIBRA_EM_REAL = 6.27


# Função para conversão de reais para dolares
def coverter_para_dolares(valor_em_reais):
    valor_em_dolares = valor_em_reais / VALOR_DOLAR_EM_REAL 
    return round(valor_em_dolares,2)

# Função para conversão de reais para euros
def coverter_para_euros(valor_em_reais):
    valor_em_euros = valor_em_reais / VALOR_EURO_EM_REAL  
    return round(valor_em_euros,2)

# Função para conversão de reais para libras
def coverter_para_libras(valor_em_reais):
    valor_em_libras = valor_em_reais / VALOR_LIBRA_EM_REAL
    return round(valor_em_libras,2)


def menu():
    valor_em_reais = float(input("Informe o valor em Reais: ")) 
    opcao = 0

    while((opcao != 1) and (opcao != 2) and (opcao != 3)):
        print(" 1 - Converter Reais em Dolares ")
        print(" 2 - Converter Reais em Euros ")
        print(" 3 - Converter Reais em Libras ")
        opcao = int(input())

        if(opcao == 1):
            valor_em_dolares = coverter_para_dolares(valor_em_reais)
            print(f"Valor em reais {valor_em_reais} convertido em dolares {valor_em_dolares}")
        elif(opcao == 2):
            valor_em_euros = coverter_para_euros(valor_em_reais)
            print(f"Valor em reais {valor_em_reais} convertido em euros {valor_em_euros}")
        elif(opcao == 3):
            valor_em_libras = coverter_para_libras(valor_em_reais)
            print(f"Valor em reais {valor_em_reais} convertido em libras {valor_em_libras}")
        else:
            print("Opção Inválida !!!")


def main():
    menu()


if __name__ == ("__main__"):
    main()
