#biblioteca
import function

fileiras = 12
cadeiras = 8
cinema = function.geraCadeiras(fileiras, cadeiras)

# listas
cadastros = list()
reservas = list()
usuario = ""

# arquivos
arquivo_dados_clientes = "Dados_clientes.txt"

# criar arquivos

# Para parar o codigo informe, escolha = 0
try:
    while True:
        function.mostraMenu()
        escolha = int(input("Informe a opção que deseja: "))
        if escolha == 0:
            break

        if escolha == 1:
            usuario = (function.cadastrar_cliente())
            if usuario == False:
                print('\033[1;90m=\033[m' * 56)
                print('\nCPF já registrado!\n')
            else:
                with open(f'{arquivo_dados_clientes}', 'a') as arquivo:
                    arquivo.write(str(usuario) + '\n')

        if escolha == 2:
            while True:
                cpf = str(input("Informe o CPF do cliente: "))
                if len(cpf) != 11:
                    print('Informe o CPF no padrão (xxx.xxx.xxx-xx): ')
                if len(cpf) == 11:
                    break

            getCPF = function.getCPF(cpf)
            if getCPF == None:
                print('\033[1;90m=\033[m' * 56)
                print('\nCPF não cadastrado!\n')
            else:
                print('\033[1;90m=\033[m' * 56)
                function.consulta_cliente(cpf)

        if escolha == 3:
            function.imprimeCadeiras(cinema)
            while True:
                cpf = str(input("Informe o CPF do cliente: "))
                if len(cpf) != 11:
                    print('Informe o CPF no padrão (xxx.xxx.xxx-xx): ')
                if len(cpf) == 11:
                    break
            consultaCPF = function.getCPF(cpf)
            if consultaCPF == True:
                while True:
                    fileira = input('Informe a fileira: ')
                    cadeira = input('Informe a cadeira: ')
                    fileiraNum = int(fileira)
                    cadeiraNum = int(cadeira)
                    if fileiraNum <= 12 and cadeiraNum <= 8:
                        break
                    else:
                        print('Informe uma fileira e cadeira existente ')
                consulta = function.consultaDisponibilidade(fileira, cadeira)
                if consulta == False:
                    function.cadastraReserva(cpf, fileira, cadeira)
                    print('\033[1;90m=\033[m' * 56)
                    print('\nSuccessful\n')
                    function.AdicionaEmRelatorioReservas(fileira, cadeira, cpf)
                    MatrizCL = function.FazMatrizParaRelatorioCadeirasLivres()
                    reservaCL = f'[{fileira}, {cadeira}]'
                    function.AdcionaEmReservasAtuais(reservaCL)
      
                else:
                    print('\033[1;90m=\033[m' * 56)
                    print('\nCadeira já reservada!\n')

            else:
                print('\033[1;90m=\033[m' * 56)
                print('\nCPF não cadastrado!\n')

        if escolha == 4:
            while True:
                cpf = str(input("Informe o CPF do cliente: "))
                if len(cpf) != 11:
                    print('Informe o CPF no padrão (xxx.xxx.xxx-xx): ')
                if len(cpf) == 11:
                    break
            fileira = int(input('Informe a fileira: '))
            cadeira = int(input('Informe a cadeira: '))
            consulta = function.consultaDisponibilidade(fileira, cadeira)
            if consulta == True:
                consultaCPF = function.getCPF(cpf)
                if consultaCPF == True:
                    function.cancelaReserva(cpf, fileira, cadeira)
                    reserva = f'[{fileira}, {cadeira}]'
                    function.AtualizaReservasAtuais(reserva)
                    print('\033[1;90m=\033[m' * 56)
                    print('\nSuccessful\n')
                    function.AdicionaEmRelatoriocancelamento(
                        fileira, cadeira, cpf)
                    
                else:
                    print('\033[1;90m=\033[m' * 56)
                    print('\nCPF não cadastrado!\n')
            else:
                print('\033[1;90m=\033[m' * 56)
                print('\nCadeira não está reservada!\n')

        if escolha == 5:
            function.RelatorioDeReservas()

        if escolha == 6:
            reservas2 = function.getReservas()
            matriz = function.FazMatrizParaRelatorioCadeirasLivres()
            novamatriz = function.RetiraDaMatriz(matriz,reservas2)
            function.AdcionaEmRelatorioCadeirasLivres(novamatriz)
            function.printRelatorioCadeirasLivres()
        if escolha == 7:
            function.RelatorioDeCancelamento()

except ValueError:
    print('Erro...')
