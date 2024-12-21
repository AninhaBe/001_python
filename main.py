# Print + input
nome = input("Digite seu nome: ")
print(f'{nome} tem {len(nome)} caracteres')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

# recebendo entradas
def soma(a, b):
   print(a + b) 

soma(2, 2)

a = int(input("Digite um número: "))
b = int(input("Digite o utro número: "))
print("Resultado = " + str(a + b))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

# Cálculo de Bônus com Entrada do Usuário
# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o valor do seu salário mensal: "))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o valor recebido do bônus: "))
# 4) Calcule o valor do bônus final
# # 5) Imprima cálculo do KPI para o usuário
recebido = 1000 + salario * bonus

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'Olá, {nome}! o seu bônus foi de {recebido}')
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?