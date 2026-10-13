def calcular_media(lista_de_notas):
    return sum(lista_de_notas) / len(lista_de_notas)

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

notas = []

# 1. Cadastro de Notas
while True:
    entrada = input("Digite a nota (ou 'fim' para sair): ")

    if entrada.lower() == "fim":
        if len(notas) > 0:
            break
        print("Digite pelo menos uma nota antes de sair!")
        continue

    # Verificação de texto vs. número e limite de 1 a 10
    try:
        nota = float(entrada)
        if 1 <= nota <= 10:
            notas.append(nota)
        else:
            print("Erro: A nota deve estar entre 1 e 10.")
    except ValueError:
        print("Erro: Digite apenas números válidos (ex: 7.5) ou 'fim'.")

# 2. Cálculo da Média (chamando a função)
media = calcular_media(notas)

# 3. Determinação da Situação
situacao = verificar_situacao(media)

# 4. Relatório Final
print("\n--- RELATÓRIO FINAL ---")
print("Notas inseridas:")
for nota in notas:
    print(f"- {nota}")

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")