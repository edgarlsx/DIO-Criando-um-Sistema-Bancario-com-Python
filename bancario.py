import locale

# Configura o formato de moeda para R$
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Variáveis iniciais
saldo = 0.00
depositos = []
saques = []
limite_saque_diario = 3
saque_maximo = 500.00
saques_realizados = 0

# Função para exibir o saldo formatado como moeda
def formatar_moeda(valor):
    return locale.currency(valor, grouping=True)

# Função de depósito
def deposito():
    global saldo
    valor = float(input("Informe o valor do depósito: R$ "))
    if valor > 0:
        depositos.append(valor)
        saldo += valor
        print(f"Depósito de {formatar_moeda(valor)} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")

# Função de saque
def saque():
    global saldo, saques_realizados
    if saques_realizados >= limite_saque_diario:
        print("Limite de saques diários atingido.")
        return
    
    valor = float(input("Informe o valor do saque: R$ "))
    if valor > saldo:
        print("Não será possível sacar o dinheiro por falta de saldo.")
    elif valor > saque_maximo:
        print(f"Limite máximo por saque é {formatar_moeda(saque_maximo)}.")
    elif valor > 0:
        saques.append(valor)
        saldo -= valor
        saques_realizados += 1
        print(f"Saque de {formatar_moeda(valor)} realizado com sucesso!")
    else:
        print("Valor de saque inválido.")

# Função para exibir o extrato
def extrato():
    print("\n--- Extrato ---")
    
    print("\nDepósitos:")
    if not depositos:
        print("Nenhum depósito realizado.")
    else:
        for i, valor in enumerate(depositos, 1):
            print(f"{i} - {formatar_moeda(valor)}")

    print("\nSaques:")
    if not saques:
        print("Nenhum saque realizado.")
    else:
        for i, valor in enumerate(saques, 1):
            print(f"{i} - {formatar_moeda(valor)}")
    
    print(f"\nSaldo atual: {formatar_moeda(saldo)}\n")

# Função principal
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            deposito()
        elif opcao == "2":
            saque()
        elif opcao == "3":
            extrato()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()
