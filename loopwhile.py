op = -1 

while op != 4:  #enquanto op for diferente de 0, o loop continua        
    #exibicao do menu
    print("Menu de opções:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")
    print("4. Sair")
    op = int(input("Informe sua opcao: ")) #leitura da opcao do usuario
    
    print("/n") #pula uma linha

    #vericacao das opcoes disponiveis 
    if op == 1:
        print("opcao 1 selecionada")
    elif op == 2:
        print("opcao 2 selecionada")
    elif op == 3:   
        print("opcao 3 selecionada")
    

    print ("OK! O programa terminou") #mensagem exibida quando o usuario escolhe a opcao 4 e o loop termina