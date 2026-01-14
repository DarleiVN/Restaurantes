import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza_Suprema', 'categoria':'Italiana', 'ativo':True}, 
                {'nome':'Burger_Master', 'categoria':'Americana', 'ativo':False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo...\n')
    print('Aplicativo finalizado com sucesso!')

def voltar_ao_menu_principal():
    input('Pressione Enter para voltar ao menu principal...')
    main()
    

def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(f'{linha}')
    print(f'{texto}\n')
    print(linha)
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('cadastrando de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do {nome_do_restaurante} que deseja cadastrar: ')
    ativo = False  # Novo restaurante começa como inativo
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': ativo}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
    
def listar_restaurantes():

    exibir_subtitulo('listando restaurantes\n')
    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(22)} | Status')
    if not restaurantes:
        print('Nenhum restaurante cadastrado.\n')
    else:
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = restaurante['ativo']
            
            print(f'->{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | Ativo: {"Sim" if restaurante["ativo"] else "Não"}')
        
        voltar_ao_menu_principal()

def alterar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    
    for restaurante in restaurantes:
        if nome_do_restaurante.lower() == restaurante['nome'].lower():
            restaurante['ativo'] = not restaurante['ativo']
            estado = 'ativo' if restaurante['ativo'] else 'inativo'
            print(f'Restaurante "{restaurante["nome"]}" agora está {estado}.\n')
            break
    else:
        print(f'Restaurante "{nome_do_restaurante}" não encontrado.\n')
           
 
    voltar_ao_menu_principal()   
     
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
            
        elif opcao_escolhida == 4:
            finalizar_app()
            return False  # encerra o loop
        else:
            print('Opção inválida!\n')
    except ValueError:
        print('Entrada inválida! Digite apenas números.\n')
    return True  # continua o loop

def main():
    continuar = True
    while continuar:
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opcoes()
        continuar = escolher_opcao()
        if continuar:
            input('Pressione Enter para voltar ao menu...')

if __name__ == '__main__':
    main()