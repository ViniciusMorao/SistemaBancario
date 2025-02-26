# Sistema Bancário em Python

Este projeto é um sistema bancário simples desenvolvido em Python como parte do **Curso Suzano Python Developer** na plataforma DIO (Digital Innovation One). O programa simula operações básicas de um banco, como depósitos, saques e consulta de extrato, sendo ideal para quem está aprendendo os conceitos fundamentais de Python.

---

## Funcionalidades

### Versão 2 (Aprimorada)
A versão 2 do sistema bancário traz melhorias significativas em relação à versão inicial, com novas funcionalidades e uma estrutura de código mais organizada e modularizada. Abaixo estão as principais melhorias:

#### Novas Funcionalidades
1. **Adicionar Cliente:**
   - Permite cadastrar novos clientes com informações como nome, CPF, data de nascimento e endereço.
   - Verifica se o CPF já está cadastrado para evitar duplicidades.

2. **Adicionar Conta:**
   - Cria uma nova conta bancária vinculada a um cliente existente.
   - Cada conta possui um número único e pertence a uma agência específica.

3. **Mostrar Contas:**
   - Exibe todas as contas cadastradas, com detalhes como agência, número da conta e nome do titular.

4. **Modularização do Código:**
   - O código foi dividido em funções específicas, como `depositar`, `sacar`, `exibir_extrato`, `adicionar_cliente`, `criar_conta` e `mostrar_contas`.
   - Isso melhora a legibilidade, manutenção e escalabilidade do código.

5. **Uso de Dicionários:**
   - As informações dos clientes e contas são armazenadas em dicionários, o que facilita o gerenciamento e a consulta dos dados.

6. **Validações Aprimoradas:**
   - Adição de validações para garantir que operações como depósito e saque sejam realizadas apenas com valores válidos.

---
