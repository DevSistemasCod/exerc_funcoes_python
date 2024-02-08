
# Calcular a média de dois números
def calcular_media(numero_alunos, quantidade_provas):
    total_notas = 0;
    media = 0
    nota_prova = 0

    for i in range(1, numero_alunos+1):
        for j in range(1, quantidade_provas+1):
            print(f"Informe a nota {j} do aluno {i}: ")
            nota_prova = float(input())
            total_notas = total_notas + nota_prova
        
        media = round((total_notas/quantidade_provas),2)
        print(f"Aluno{i} media {media}")


def main():
    numero_alunos = int(input("Informe o número de alunos: "))
    quantidade_provas = int(input("Informe a quantidade de provas: "))

    calcular_media(numero_alunos, quantidade_provas)

if __name__ == "__main__":
    main()
