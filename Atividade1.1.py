# # 1. Crie um programa que o usuario possa digitar quantos numeros quiser e ao terminar imprima a lista em ordem crescente.


# # 2. Crie um programa que o usuario possa digitar a quantidade desejada de notas de um determinado aluno( nota minima 0 e nota maxima 10) e o programa calcula a media desse aluno, e
# #  ao final imprima se o aluno está(aprovado>=/, reprovado e recuperação >= 5)

# #NOTE - Atividade 1

# # numeros = []
# # print("Digite um número que deseja adicionar(se não for adicionar mais escreva 'sair': ")
# # while True:
# #     entrada = input("Digite um numero: ").strip().lower()
# #     if entrada == 'sair':
# #         break

# #     try:
# #         numero = float(entrada)
# #         numeros.append(numero)
# #     except ValueError:
# #         print("Entrada inválida, digite um número válido ou escreva 'sair'. ")

# # numeros.sort()

# # print("\n--- Resultado ---")
# # print(f"Lista ordenada: {numeros}")

# #NOTE - Atividade 2

notas = [] 

nome = input("Digite o seu nome: ")
curso = input("Qual o seu curso técnico? ")

print(f"\nOlá {nome}, do curso {curso}. Digite as notas abaixo:")
print("(Para encerrar e ver a média, escreva 'sair')")

while True:
    entrada = input("Digite a nota: ").strip().lower()
    
    if entrada == 'sair': 
        break 
        
    try:

        valor_nota = float(entrada)
     
        if 0 <= valor_nota <= 10:
            notas.append(valor_nota) 
        else:
            print("A nota deve estar entre 0 e 10.")
            
    except ValueError:
        print("Entrada inválida! Digite um número ou 'sair'.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"\n--- Boletim de {nome} ---")
    print(f"Média Final: {media:.2f}")
    
    if media >= 7:
        print("Status: APROVADO")
    elif media >= 5:
        print("Status: RECUPERAÇÃO")
    else:
        print("Status: REPROVADO")
else:
    print("Nenhuma nota foi registrada.")
