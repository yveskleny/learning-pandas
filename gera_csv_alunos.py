import csv

# Lista de alunos e notas
alunos = [
    {"nome": "Ana", "nota1": 8.5, "nota2": 7.0},
    {"nome": "Bruno", "nota1": 6.0, "nota2": 5.5},
    {"nome": "Carla", "nota1": 9.0, "nota2": 8.5},
    {"nome": "Diego", "nota1": 4.0, "nota2": 6.0},
    {"nome": "Eduarda", "nota1": 7.5, "nota2": 8.0},
]

# Criando o arquivo CSV
with open("notas_finais.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")
    
    # Cabeçalho
    escritor.writerow(["Nome", "Nota 1", "Nota 2", "Nota Final"])
    
    # Linhas com dados
    for aluno in alunos:
        nota_final = (aluno["nota1"] + aluno["nota2"]) / 2
        escritor.writerow([aluno["nome"], aluno["nota1"], aluno["nota2"], round(nota_final, 2)])

print("Arquivo 'notas_finais.csv' gerado com sucesso!")
