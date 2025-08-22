# Simulador de Caixa Eletrônico
# Autor: Gabriel Rodrigues
# Data: 14/08/2025
# Descrição: Sistema simples de caixa de loja com funções, validações e histórico.


# Dados iniciais do sistema
usuarios = {
    "mercadinho": {
        "Saldo": 1000,
        "Entradas": {"Venda": 0, "Emprestimo": 0, "Investimento": 0, "Outros:": 0}, 
        "Saídas": {"Gastos Operacionais": 0, "Despesas Administrativas": 0, "Compra de mercadoria": 0, "Outros:": 0},
        "senha": "1234"
        },
    "farmacia": {
        "Saldo": 2900,
        "Entradas": {"Venda": 0, "Emprestimo": 0, "Investimento": 0, "Outros:": 0},
        "Saídas": {"Gastos Operacionais": 0, "Despesas Administrativas": 0, "Compra de mercadoria": 0, "Outros:": 0},
        "senha": "1234"
        }
}

# Inicializando o sistema
def login():
    while True:
        print("Digite seu usuário ou Digite * para voltar ao menu.")
        usuario = input("\nUsuário: ").strip()
        if usuario.lower() == "*":
            return False

        if usuario in usuarios:
            tentativas = 3
            while tentativas > 0:
                senha = input("Senha: ").strip()
                if senha == usuarios[usuario]["senha"]:
                    print(f"\n✅ Login bem-sucedido! Bem-vindo, {usuario}.")
                    return True
                else:
                    tentativas -= 1
                    print(f"❌ Senha incorreta! Tentativas restantes: {tentativas}")
            print("\n⚠ Você errou a senha 3 vezes. Voltando ao menu principal...")
            return False
        else:
            print("❌ Usuário não encontrado.")
            print("\nTente novamente ou digite '*' para cadastrar um novo usuário.")

def cadastrar_usuario():
    print("\n=== CADASTRO DE NOVO USUÁRIO ===")
    novo_usuario = input("Digite o novo login: ").strip().lower()
    if novo_usuario in usuarios:
        print("⚠ Usuário já existe!")
        return
    nova_senha = input("Digite sua nova senha: ").strip()
    usuarios[novo_usuario] = {
        "Saldo": 0,
        "Entradas": {"Venda": 0, "Emprestimo": 0, "Investimento": 0, "Outros": 0},
        "Saídas": {"Gastos Operacionais": 0, "Despesas Administrativas": 0, "Compra de mercadoria": 0, "Outros": 0},
        "senha": nova_senha
    }
    print(f"✅ Usuário {novo_usuario} cadastrado com sucesso!")

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("\n===   1 - LOGIN    ===")
        print("\n===  2 - CADASTRO  ===")
        print("\n===   3 -  SAIR    ===")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            if login():
                print("TESTE OK")
            
        elif opcao == "2":
                cadastrar_usuario()
            
        elif opcao == "3":
                print("Saindo...")
                break
        else:
                print("⚠ Opção inválida! Tente novamente.")

menu_principal()
