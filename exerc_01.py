
# Método para calcular a Média de 3 Notas
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return round(media,2)

# Método Principal
def main():
    print(" Informe as notas: ")
    nota1 = float(input("Informe a nota 1: "))
    nota2 = float(input("Informe a nota 2: "))
    nota3 = float(input("Informe a nota 3: "))
    resultado = calcular_media(nota1, nota2, nota3)
    print("Saída da média: ",resultado)

if __name__ == "__main__":
    main()