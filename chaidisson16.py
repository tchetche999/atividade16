# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.
situacao = input("Você é idoso, gestante, cadeirante ou nenhum destes? Digite 'idoso', 'gestante', 'cadeirante' ou 'nenhum': ")
if situacao == "idoso" or situacao == "gestante" or situacao == "cadeirante":
    print("Você tem acesso à fila de prioridade.")
else:
    print("Você não tem acesso à fila de prioridade.")