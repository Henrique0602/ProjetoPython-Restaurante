import os


restaurantes=[{'nome':'Praça', 'categoria':'japonesa', 'ativo':False}, 
              {'nome':'Casa da Vo', 'categoria': 'Caseira', 'ativo':True},
              {'nome':'Pizzaria Insana', 'categoria':'Pizza', 'ativo':False}]   

def exibir_nome_do_programa():
     print('Sabor Express\n')

def exibir_opcoes():
     print('1. Cadastrar restaurtante')
     print('2. Listar restaurante')
     print('3. Mudar estado do restaurtante')
     print('4. Sair\n')

def finalizar_app():
       os.system("cls")
       print('Encerrando o programa')
      
def exibir_subtitulo(texto):
     os.system('cls')
     linha = '*' * (len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()

     
def opcao_invalida():
     print('opcao inválida\n')
     input('Digite uma tecla para voltar ao menu principal: ')
     main()


def  cadastrar_novo_restaurante():
     """Essa função é responsavel por cadastrar novo restaurante """
     os.system('cls')
     exibir_subtitulo('Cadastro de novo restaurante\n')

     nome_do_restaurante = input('Digite o nome do restaurente que deseja cadastrar: ')
     categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante} : ')
     dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
     restaurantes.append(dados_do_restaurante)
     print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

     input('Digite uma tecla para voltar para o menu principal')

     main()

def  listar_restaurantes():
     """Essa função é responsavel por listar todos os restaurantes"""
     os.system('cls')
     exibir_subtitulo('Listagem dos restaurantes\n')

     print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | Status')
     for restaurante in restaurantes:
          nome_restaurante = restaurante['nome']
          categoria = restaurante['categoria']
          ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
          print(f'. {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}' )
     input('Digite uma tecla para voltar para o menu principal')
     main()


def alternar_estado_restaurante():
    """Essa função é responsavel por alterar o estado dos restaurantes"""
    exibir_subtitulo('Vamos mudar o estado do seu restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja mudar o estado : ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
         if nome_restaurante == restaurante['nome']:
              restaurante_encontrado = True
              restaurante['ativo'] = not restaurante['ativo']
              mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaraunte {nome_restaurante} foi desativado com sucesso'
              print(mensagem)
    
    if not restaurante_encontrado:
         print("o restaurante nao foi encontrado")

    input('Digite uma tecla para voltar para o menu principal')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()   
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except: 
            opcao_invalida()
    

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':

    main()




