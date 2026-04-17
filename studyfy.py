# INÍCIO
print("\nSTUDYFY")
print("Onde todo o estudante tem espaço para aprender!")

# CRIAR CONTA // FAZER LOGIN
resposta = input("\nVocê já possuí conta? S/N: ")

temConta = resposta == "S"

if temConta:
    print("\n --- LOGIN ---")

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
print("\n--- MENU ---")

while True:
    print("1. Cadastrar tarefa")
    print("2. Listar tarefas")
    print("3. Ver tarefas urgentes")
    print("4. Marcar tarefa como concluída")
    print("5. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 5:
        print("Saindo")
    break  

    elif opcao == '1':
    
    elif opcao == '2':
    
    elif opcao == '3':
 
    elif opcao == '4':

    else:
    print("Opção Inválida, tente novamente!")