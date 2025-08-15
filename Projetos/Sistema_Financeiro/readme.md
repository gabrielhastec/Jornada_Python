
# 🏧 Simulador de Caixa Eletrônico

> **Status:** Em desenvolvimento (Versão 0.1)
> **Autor:** Gabriel Rodrigues
> **Data de Início:** 14/08/2025
> **Licença:** MIT (a ser adicionada)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Licença](https://img.shields.io/badge/Licença-MIT-green)
![Versão](https://img.shields.io/badge/Versão-0.1-orange)

## 📑 Sumário

* [Descrição](#-descrição)
* [Funcionalidades](#-funcionalidades)

  * [Implementadas](#-implementadas)
  * [Planejadas](#-planejadas)
* [Estrutura do Projeto](#️-estrutura-do-projeto)
* [Como Executar](#-como-executar)
* [Como Usar](#-como-usar)
* [Limitações Atuais](#️-limitações-atuais)
* [Contribuição](#-contribuição)
* [Licença](#-licença)
* [Contato](#-contato)

---

## 📖 Descrição

O **Simulador de Caixa Eletrônico** é um projeto em **Python** que simula um sistema simples de gerenciamento financeiro para lojas, com interface via **console**.

📌 **Objetivos principais**:

* Servir como projeto de aprendizado.
* Ter código simples, modular e expansível.
* Evoluir gradualmente para incluir funcionalidades completas de transações financeiras.

---

## ✨ Funcionalidades

### ✅ Implementadas

* 🔐 **Login de Usuário** — autenticação com limite de 3 tentativas e opção de voltar ao menu com `*`.
* 📝 **Cadastro de Usuário** — criação de novas contas com login e senha.
* 📋 **Menu Principal** — interface interativa com opções de login, cadastro e saída.

### 🔜 Planejadas

* 💸 **Gerenciamento de Transações** — registro de entradas e saídas.
* 📜 **Histórico de Transações** — exibição filtrada por usuário.
* 💰 **Consulta de Saldo** — saldo atual por conta.
* 💾 **Persistência de Dados** — uso de **JSON** para salvar informações.
* 🔒 **Segurança** — hashing de senhas e validação de senha forte.
* 🖼️ **Interface Gráfica** — integração futura com Tkinter ou similar.

---

## 🗂️ Estrutura do Projeto

```
Sistema_Financeiro/
│
├── sistema_caixa.py   # Arquivo principal
└── README.md             # Documentação
```

### Estrutura de Dados

* **Dicionário `usuarios`** contendo:

  * `saldo`: valor inicial da conta.
  * `entradas`: receitas categorizadas.
  * `saidas`: despesas categorizadas.
  * `senha`: senha em texto plano (temporário).

### Funções Principais

* `login()` → gerencia autenticação.
* `menu_principal()` → exibe as opções do sistema.
* `cadastrar_usuario()` → cria novos usuários.

---

## 🚀 Como Executar

### Pré-requisitos

* Python **3.x** instalado.
* Nenhuma dependência externa.

### Passos

```bash
# 1. Clone ou baixe o repositório
git clone <URL_DO_REPOSITORIO>

# 2. Acesse o diretório do projeto
cd Sistema_Financeiro

# 3. Execute o script
python sistema_caixa.py
```

---

## 📌 Como Usar

* **1** → Fazer login (`usuario: mercadinho`, `senha: 1234` para teste).
* **2** → Cadastrar novo usuário.
* **3** → Sair.

💡 No login, digite `*` para voltar ao menu.

---

## ⚠️ Limitações Atuais

* Funções financeiras ainda não implementadas.
* Senhas armazenadas sem criptografia.
* Interface apenas no console.

---

## 🤝 Contribuição

1. Faça um **fork** do projeto.
2. Crie uma branch:

   ```bash
   git checkout -b minha-feature
   ```
3. Faça commits:

   ```bash
   git commit -m "Adiciona nova funcionalidade"
   ```
4. Envie para seu repositório:

   ```bash
   git push origin minha-feature
   ```
5. Abra um **Pull Request**.

---

## 📜 Licença

Distribuído sob a licença **MIT**.
Arquivo de licença será adicionado futuramente.

---

## 📧 Contato

* **Autor:**  *Gabriel Rodrigues*
* **E-mail:** *gabrielhastec.dev@gmail.com*
* **GitHub:** *[Gabriel Hastec](https://github.com/gabrielhastec)*

⭐ Obrigado por conferir o **Simulador de Caixa Eletrônico**!

---
