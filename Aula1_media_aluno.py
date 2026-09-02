

#Def é uma função que recebe parâmetros e retorna um valor, ela pode ser chamada em qualquer parte do código, desde que seja declarada antes da chamada.
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


print("Bem vindo, ao programa de cálculo de média do aluno!")
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = calcular_media(nota1, nota2)

if media >= 7:
    situação = "Aprovado"
elif media >= 5:
    situação = "Recuperação"    
else:
    situação = "Reprovado"  

print(f" Nome: {nome} ")
print(f" Nota 1: {nota1:.1f} ")
print(f" Nota 2: {nota2:.1f} ")
print(f" Média: {media:.2f} ")
print(f" Situação: {situação} ")


#script para calcular a média de vários alunos usando pandas

import pandas as pd

dados = {
    "Aluno": ["Ana", "Bruno", "Carlos", "Maria"],
    "Nota1": [8.0, 5.0, 7.0, 9.0],
    "Nota2": [7.0, 6.0, 8.0, 8.5],
    "Nota3": [9.0, 4.0, 6.5, 10.0]
}

alunos = pd.DataFrame(dados)

alunos["Media"] = (
    alunos["Nota1"] +
    alunos["Nota2"] +
    alunos["Nota3"]
) / 3

alunos["Situacao"] = alunos["Media"].apply(
    lambda media: "Aprovado" if media >= 7 else "Reprovado"
)

print(alunos)


#script 2 

numeros = []
pares = 0

print("--- Análise de Sequência Numérica ---")
print("Digite números inteiros positivos. Digite 0 para encerrar e ver os resultados.\n")

# Estrutura de repetição para entrada de dados
while True:
    
    num = int(input("Digite um número: "))

    # Estrutura de decisão para encerrar o loop
    if num == 0:
        break

    
    numeros.append(num)

    # Estrutura para contar os números pares
    if num % 2 == 0:
        pares += 1

# Processamento e Saída de dados (apenas se a lista não estiver vazia)
if len(numeros) > 0:
    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    # Saídas de dados com os resultados
    print("\n====== RESULTADOS ======")
    print(f"Soma de todos os números: {soma}")
    print(f"Média dos números: {media:.2f}")
    print(f"Quantidade de números pares: {pares}")
    print(f"Maior valor digitado: {maior}")
    print(f"Menor valor digitado: {menor}")
else:
    print("\nNenhum número válido foi digitado.")






#Script 3
def calcular_preco_final(valor_compra, tipo_cliente):
    
    if tipo_cliente.upper() == "VIP":
        percentual = 0.15  # 15% de desconto
    elif tipo_cliente.upper() == "REGULAR":
        percentual = 0.05  # 5% de desconto
    else:
        percentual = 0.0  # Sem desconto

    desconto = valor_compra * percentual
    return valor_compra - desconto 

print("Bem-vindo ao programa de cálculo de preço final!")
valor_compra = float(input("Digite o valor da compra: "))
tipo_cliente = input("Digite o tipo de cliente (VIP/Regular/Outro): ")
preco_final = calcular_preco_final(valor_compra, tipo_cliente)



#Script 4 
#Lista aluno vazia
cadastro_alunos = []

print("--- Cadastro e Classificação de Alunos ---")
print("Digite os dados solicitados. Digite 'fim' no nome para encerrar.\n")

# Estrutura de repetição para o cadastro de múltiplos alunos
while True:
    # Entrada de dados
    nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    
    # Estrutura de decisão para parar o cadastro
    if nome.lower() == "fim":
        break
        
    nota = float(input(f"Digite a nota final de {nome}: "))

    # Estrutura de decisão para classificar o aluno por desempenho
    if nota >= 9.0:
        classificacao = "Excelente"
    elif nota >= 7.0:
        classificacao = "Bom"
    elif nota >= 5.0:
        classificacao = "Regular"
    else:
        classificacao = "Insuficiente"

    # Criação do dicionário com as informações do aluno atual
    aluno = {
        "nome": nome,
        "nota": nota,
        "classificacao": classificacao
    }

    # Armazena o dicionário do aluno na lista geral
    cadastro_alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")

# Estrutura de repetição para exibir o relatório final (Saída de dados)
print("\n====== RELATÓRIO FINAL DE ALUNOS ======")
for a in cadastro_alunos:
    print(f"Aluno: {a['nome']} | Nota: {a['nota']:.1f} | Desempenho: {a['classificacao']}")
