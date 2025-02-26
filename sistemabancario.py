#Desenvolvendo um sistema bancário V2.
import textwrap

def menu():
  menu = """

  ========== MENU ==========

  [1] Depositar
  [2] Sacar
  [3] Extrato
  [4] Adicionar cliente
  [5] Adicionar conta
  [6] Mostrar contas
  [0] Sair

  ==========================
  => """

  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      print("Depósito realizado com sucesso!")
    else:
      print("Operação falhou! O valor é inválido.")

    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limite_saques

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
    print("Saque realizado com sucesso!")
  else:
    print("Operação falhou! O valor é inválido.")

  return saldo,extrato

def exibir_extrato(saldo, /, *, extrato):
  print("\n================ EXTRATO ================")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("==========================================")

def adicionar_cliente(usuarios):
  cpf = input("Informe o CPF (somente números): ")
  usuario = filtrar_usuario(cpf,usuarios)

  if usuario:
    print("Já existe usuário com esse CPF!")
    return

  nome = input("Informe o nome completo: ")
  data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ")
  endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

  usuarios.append({"nome" : nome,"data_nascimento" : data_nascimento, "cpf":cpf ,"endereco" : endereco})

  print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF (somente números): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Conta criada com sucesso!")
    return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
  
  print("Usuário não encontrado, criação de conta encerrado.")

def mostrar_contas(contas):
  for conta in contas:
    linha = f"""\
      Agência: {conta['agencia']}
      Numero da conta: {conta['numero_conta']}
      Titular: {conta['usuario']['nome']}
    """
    print("")
    print(textwrap.dedent(linha))

def main():
  LIMITE_SAQUES = 3
  AGENCIA = "0001"

  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  numero_conta = 1
  usuarios = []
  contas = []

  while True:
    op = menu()

    if op == "1":
      valor = float(input("Insira o valor do depósito: "))

      saldo, extrato = depositar(saldo, valor, extrato)

    elif op == "2":
      valor = float(input("Insira o valor do saque: "))

      saldo, extrato = sacar(
        saldo = saldo,
        valor = valor,
        extrato = extrato,
        limite = limite,
        numero_saques = numero_saques,
        limite_saques = LIMITE_SAQUES,
      )

    elif op == "3":
      exibir_extrato(saldo, extrato=extrato)

    elif op == "4":
      adicionar_cliente(usuarios)

    elif op == "5":
      conta = criar_conta(AGENCIA,numero_conta,usuarios)

      if conta:
        contas.append(conta)
        numero_conta += 1

    elif op == "6":
      mostrar_contas(contas)

    elif op == "0":
      break

    else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")
main()
