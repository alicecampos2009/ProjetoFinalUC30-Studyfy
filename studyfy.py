# INÍCIO
print("\nSTUDYFY")
print("Onde todo o estudante tem espaço para aprender!")

# LISTA PARA GUARDAR TAREFAS
tarefas = []

# CRIAR CONTA // FAZER LOGIN
resposta = input("\nVocê já possui conta? S/N: ").upper()

temConta = resposta == "S"

if temConta:
    print("--- LOGIN ---")

    input("Nome de Usuário: ")
    input("Senha: ")

    print("Entrando...")

else:
    print("\n--- CRIAR CONTA ---")

    input("Nome Completo: ")
    input("E-mail Institucional: ")
    input("CPF: ")
    input("Nome de Usuário: ")
    input("Criar Senha: ")

    print("Conta criada com sucesso!")

# MENU
while True:
    print("\n--- MENU ---")
    print("1. Cadastrar tarefa")
    print("2. Listar tarefas")
    print("3. Ver tarefas urgentes")
    print("4. Marcar tarefa como concluída")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    # SAIR
    if opcao == "5":
        print("Saindo...")
        break

    # CADASTRAR TAREFA
    elif opcao == "1":
        print("--- CADASTRAR TAREFA ---")
        nome = input("Nome da tarefa: ")
        urgente = input("É urgente? (s/n): ").lower()

        tarefa = {
            "nome": nome,
            "urgente": urgente == "s",
            "concluida": False
        }

        tarefas.append(tarefa)
        print("Tarefa cadastrada com sucesso!")

    # LISTAR TODAS
    elif opcao == "2":
        print("--- LISTAR TAREFAS ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")

    # VER URGENTES
    elif opcao == "3":
        pass

    # MARCAR COMO CONCLUÍDA
    elif opcao == "4":
        pass

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida, tente novamente!")