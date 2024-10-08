from database.mongohandler import Operations
from database.entities import User, Message

if __name__ == "__main__":
    operations = Operations()

    while True:
        print("Escolha uma opção:")
        print("1. Fazer login")
        print("2. Cadastrar novo usuário")
        print("3. Sair")
        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            nickname_from = input("Digite seu nickname: ")
            password = input("Digite sua senha: ")

            login_sucesso = operations.validate_login(nickname_from, password)
            if login_sucesso:
                print("Login bem-sucedido!")
                while True:
                    print("Escolha uma opção:")
                    print("1. Enviar mensagem")
                    print("2. Ver mensagens recebidas")
                    print("3. Sair")
                    opcao = input("Digite o número da opção: ")

                    if opcao == "1":
                        nickname_to = input("Digite o nickname do destinatário: ")
                        content = input("Digite o conteúdo da mensagem: ")

                        message = Message(nickname_from=nickname_from, nickname_to=nickname_to, content=content)
                        operations.add_new_message(message)
                        print("Mensagem enviada com sucesso!")

                    elif opcao == "2":
                        nickname_sender = input("Digite o nickname da pessoa de quem você quer ver as mensagens: ")
                        messages = operations.get_messages_from(nickname_sender, nickname_from)
                        if messages:
                            print(f"Mensagens de {nickname_sender}:")
                            for msg in messages:
                                print(f"- {msg['content']}")
                        else:
                            print(f"Não há mensagens de {nickname_sender}.")

                    elif opcao == "3":
                        print("Saindo...")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("Nickname ou senha incorretos.")

        elif opcao == "2":
            nickname = input("Digite seu nickname: ")
            email = input("Digite seu email: ")
            password = input("Digite sua senha: ")

            new_user = User(nickname=nickname, email=email, password=password)
            cadastro_sucesso = operations.add_new_user(new_user)
            if cadastro_sucesso:
                print("Cadastro realizado com sucesso!")
            else:
                print("Erro: Usuário já cadastrado ou problema no cadastro.")

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
