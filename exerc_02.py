# Função para Verificar se um Número é Par
def verificar_se_par(numero):
    resto = numero % 2

    if(resto == 0):
        mensagem = "O número é par."
        return mensagem
    
    else:
        mensagem = "O número é ímpar."
        return mensagem 

# Função Principal
def main():
    numero = float(input("Informe um número: "))
    saida = verificar_se_par(numero)
    print(saida)

if __name__ == "__main__":
    main()
