#Desenvolvendo um sistema bancário.

menu = """

========== MENU ==========

      [1] Depósitar
      [2] Sacar
      [3] Extrato
      [0] Sair

==========================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  op = input(menu)

  if op == "1":
    valor = float(input("Insira o valor do depósito: "))

    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
      print("Operação falhou! O valor é inválido.")

  elif op == "2":
    valor = float(input("Insira o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >=LIMITE_SAQUES

    if excedeu_saldo:
      print("Operação falhou! Você não possui saldo suficiente.")
    elif excedeu_limite:
      print("Operação falhou! Valor do saque excede o limite.")
    elif excedeu_saques:
      print("Operação falhou! Número máximo de saques.")
    elif saldo > 0:
      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1
    else:
      print("Operação falhou! O valor é inválido.")

  elif op == "3":
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

  elif op == "0":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")