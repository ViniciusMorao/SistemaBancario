# Sistema Bancário em Python

Este projeto é um sistema bancário simples desenvolvido em Python como parte do Curso **Suzano Python Developer** na plataforma DIO (Digital Innovation One). O programa simula operações básicas de um banco, como depósitos, saques, consulta de extrato, criação de contas e gerenciamento de clientes. Ideal para quem está aprendendo os conceitos fundamentais de Python e programação orientada a objetos (POO).

---

## Funcionalidades

### Versão 3 (Aprimorada e Modularizada)

A versão 3 do sistema bancário traz melhorias significativas em relação às versões anteriores, com novas funcionalidades, uma estrutura de código mais organizada e modularizada, e a introdução de conceitos avançados de POO. Abaixo estão as principais melhorias:

#### Novas Funcionalidades

1. **Gerenciamento de Clientes**:
   - Cadastro de novos clientes (pessoas físicas) com informações como nome, CPF, data de nascimento e endereço.
   - Verificação de duplicidade de CPF para evitar clientes repetidos.

2. **Gerenciamento de Contas**:
   - Criação de contas correntes vinculadas a clientes existentes.
   - Cada conta possui um número único, agência padrão ("0001") e um titular (cliente).
   - Limite de saque diário e número máximo de saques configuráveis.

3. **Operações Bancárias**:
   - **Depósito**: Permite que clientes depositem valores em suas contas.
   - **Saque**: Permite que clientes sacam valores de suas contas, respeitando os limites diários e por saque.
   - **Extrato**: Exibe o histórico de transações (depósitos e saques) e o saldo atual da conta.

4. **Histórico de Transações**:
   - Todas as transações (depósitos e saques) são registradas com data e hora, permitindo que os clientes visualizem seu extrato.

5. **Menu Interativo**:
   - Interface de linha de comando para facilitar a navegação e execução das operações.

6. **Modularização do Código**:
   - O código foi organizado em classes e métodos específicos, como `Cliente`, `Conta`, `ContaCorrente`, `Transacao`, `Historico`, entre outros.
   - Isso melhora a legibilidade, manutenção e escalabilidade do código.

7. **Validações Aprimoradas**:
   - Adição de validações para garantir que operações como depósito e saque sejam realizadas apenas com valores válidos.
   - Verificação de limites de saque e número máximo de saques diários.
  
---

## Contribuições
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o sistema bancário.
