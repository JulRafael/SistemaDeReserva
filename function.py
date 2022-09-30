def geraCadeiras(x, y):
    matrizCinema = list()
    for i in range(x):
        fila = list()
        for j in range(y):
            fila.append('X')
        matrizCinema.append(fila)
    return matrizCinema


def imprimeCadeiras(x):
    for i in x:
        print(f'\033[32m {i} \033[0;0m')


def mostraMenu():
    menu = '\033[37mMENU\033[m'
    igual = '\033[1;90m=\033[m'
    linha = '\033[1;90m|\033[m'
    print(f"{igual*25} {menu} {igual*25}")
    print(
        f"{linha} 1 - Cadastro de Cliente \n{linha} 2 - Consulta de Clientes \n{linha} 3 - Reserva de Cadeira \n{linha} 4 - Cancelamento de Reserva de Cadeira \n{linha} 5 - Relatório de Reservas \n{linha} 6 - Relatório de Cadeiras Livres \n{linha} 7 - Relatório de Cancelamento de Reservas de Cadeiras \n{linha} 0 - Sair"
    )
    print(igual * 56)


def cadastrar_cliente():
    while True:
        cliente_cpf = str(input("Informe o CPF do cliente: "))
        if len(cliente_cpf) != 11:
            print('Informe o CPF no padrão (xxx.xxx.xxx-xx): ')
        if len(cliente_cpf) == 11:
            break
    cpf = False
    with open('Dados_clientes.txt', 'r') as arquivo:
        for c in arquivo:
            if cliente_cpf in c:
                cpf = True
    if cpf == False:
        cliente_nome = str(input('Insira o nome do cliente: ')).capitalize()
        reservas = ''
        return f'{cliente_nome}${cliente_cpf}@{reservas}/'
    else:
        erro = False
        return erro


#Informa os dados do cliente do CPF que foi passado!
def consulta_cliente(cpf):
    with open(f"{'Dados_clientes.txt'}", 'r') as arquivo:
        for c in arquivo:
            localSifrão = c.find("$")
            localArroba = c.find("@")
            localBarra = c.find("/")
            if cpf in c:
                print(f'\nNome: {c[0:localSifrão]}')
                print(f'CPF: {c[(localSifrão + 1):localArroba]}')
                if c[(localArroba + 1):localBarra] == '':
                    print(f'Reservas: Nenhuma reserva cadastrada\n')
                else:
                    print(f'Reservas: {c[(localArroba + 1):localBarra]}\n')


#Informa se a cadeira já esta reservada ou não!
def consultaDisponibilidade(x, y):
    reserva = f'[{x}, {y}]'
    with open(f"{'Dados_clientes.txt'}", 'r') as arquivo:
        consulta = False
        for i in arquivo:
            localArroba = i.find("@")
            localBarra = i.find("/")
            if reserva in i:
                consulta = True
        return consulta


def cadastraReserva(cpf, fileira, cadeira):
    reservas = f'[{fileira}, {cadeira}]'
    #Lê o arquivo e pega os dados do cliente com o cpf informado!
    with open('Dados_clientes.txt', 'r') as arquivo:
        for i in arquivo:
            localBarra = i.find("/")
            if cpf in i:
                dadosTemp = i[0:localBarra + 1]
                dados = i[0:localBarra] + reservas + '/'

    #Cria uma lista e salva todos os dados do arquivo menos do cliente que fez a reserva!
    with open('Dados_clientes.txt', 'r+') as arquivo:
        lista = []
        while True:
            dadosArquivo = arquivo.readline().strip()
            if dadosArquivo != dadosTemp:
                lista.append(dadosArquivo)
            if dadosArquivo == '':
                break
        lista.pop()
    #Limpa todas as informações do arquivo e reescreve com os dados atualizados!
    with open('Dados_clientes.txt', 'w') as arquivo:
        arquivo.write(f'{dados}\n')
        for i in lista:
            arquivo.write(f'{i}\n')


def cancelaReserva(cpf, fileira, cadeira):
    reservas = f'[{fileira}, {cadeira}]'
    with open(f'{"Dados_clientes.txt"}', 'r') as arquivo:
        for i in arquivo:
            localBarra = i.find("/")
            localReserva = i.find(reservas)
            if cpf in i:
                dadosTemp = i[0:localBarra + 1]
                dadosAtt = f'{i[0:localReserva]}{i[localReserva+6:localBarra+1]}'

    #Atualiza o Dados_clientes.txt
    with open(f'{"Dados_clientes.txt"}', 'r') as arquivo:
        salvaDados = []
        while True:
            dadosArquivo = arquivo.readline().strip()
            if dadosArquivo != dadosTemp:
                salvaDados.append(dadosArquivo)
            if dadosArquivo == '':
                break
        salvaDados.pop()
    with open(f'{"Dados_clientes.txt"}', 'w') as arquivo:
        arquivo.write(f'{dadosAtt}\n')
        for i in salvaDados:
            arquivo.write(f'{i}\n')


def getName(cpf):
    with open(f'{"Dados_clientes.txt"}', 'r') as arquivo:
        for c in arquivo:
            localDoSifrão = c.find("$")
            if cpf in c:
                return f"{c[0:localDoSifrão]}"


def getCPF(cpf):
    with open(f'{"Dados_clientes.txt"}', 'r') as arquivo:
        for c in arquivo:
            if cpf in c:
                return True


def AdicionaEmRelatorioReservas(fileira, cadeira, cpf):
    nome = getName(cpf)
    with open(f'{"Relatorio de reservas.txt"}', 'a') as arquivo:
        arquivo.write(
            f"O cliente {nome} reservou a cadeira {cadeira} na fileira {fileira}.\n"
        )


def RelatorioDeReservas():
    print("\nRelatorio de reservas feitas:\n")
    with open(f'{"Relatorio de reservas.txt"}', 'r') as arquivo:
        for c in arquivo:
            print(c.strip())
    print()


def AdicionaEmRelatoriocancelamento(fileira, cadeira, cpf):
    nome = getName(cpf)
    with open(f'{"Relatorio de cancelamento.txt"}', 'a') as arquivo:
        arquivo.write(
            f"O cliente {nome} cancelou a cadeira {cadeira} na fileira {fileira}.\n"
        )


def RelatorioDeCancelamento():
    print("\nRelatorio de cancelamento feitos:\n")
    with open(f'{"Relatorio de cancelamento.txt"}', 'r') as arquivo:
        for c in arquivo:
            print(c.strip())
    print()


def FazMatrizParaRelatorioCadeirasLivres():
    matriz = []
    for i in range(12):
        matriz.append([])
        for c in range(8):
            matriz[i].append([i + 1, c + 1])
    return matriz


def RetiraDaMatriz(matriz, reservas):
    for i in range(12):
        for c in range(8):
            for y in range(len(reservas)):
                if str(matriz[i][c]) == reservas[y]:
                    matriz[i][c] = "[***]"
    return matriz


def AdcionaEmRelatorioCadeirasLivres(matriz):
    with open('Relatorio cadeiras livres.txt', 'w') as arquivo:
        for c in range(12):
            for i in range(8):
                arquivo.write(f'{matriz[c][i]}')
            arquivo.write('\n')


def AdcionaEmReservasAtuais(reserva):
    with open(f'{"ReservasAtuais.txt"}', 'a') as arquivo:
        arquivo.write(f"{reserva}\n")


def AtualizaReservasAtuais(reserva):
    reservas = getReservas()
    for i in reservas:
        if i == reserva:
            reservas.remove(reserva)
    with open('ReservasAtuais.txt', 'w') as arquivo:
        for i in reservas:
            arquivo.write(f'{i}\n')


def getReservas():
    with open('ReservasAtuais.txt', 'r+') as arquivo:
        listaDeReservasTemp = []
        while True:
            dadosArquivo = arquivo.readline().strip()
            if dadosArquivo == "":
                break
            listaDeReservasTemp.append(dadosArquivo)
    return listaDeReservasTemp


def printRelatorioCadeirasLivres():
    with open(f'{"Relatorio cadeiras livres.txt"}', 'r') as arquivo:
        for c in arquivo:
            print(c.strip())
    print()