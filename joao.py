def chr(n):
    return "\n"

def atualizarEstado(n, estado, estadoEncomenda, tempIE, tempFE):
    estadosEncomendas()
    while True:    #This simulates a Do Loop
        opcaoestado = int(input())
        if opcaoestado > 0 and opcaoestado <= 3: break
    estadoEncomenda[n] = estado[opcaoestado]
    if estadoEncomenda[n] == estado[1]:
        print("Indique a hora de início de recolha, no formato (hora.minuto)")
        while True:    #This simulates a Do Loop
            tempI = float(input())
            if int(tempI) >= 0 or tempI <= 24 or tempI <= 8.61 or tempI <= 9.61 or tempI <= 10.61 or tempI <= 11.61 or tempI <= 12.61 or tempI <= 13.61 or tempI <= 14.61 or tempI <= 15.61 or tempI <= 16.61 or tempI <= 17.61 or tempI <= 18.61 or tempI <= 19.61: break
        tempIE[n] = tempI
    else:
        if estadoEncomenda[n] == estado[3]:
            print("Indique a hora de entrega, no formato (hora.minuto)")
            while True:    #This simulates a Do Loop
                tempF = float(input())
                if int(tempF) >= 0 or tempF <= 24 or tempF <= 8.61 or tempF <= 9.61 or tempF <= 10.61 or tempF <= 11.61 or tempF <= 12.61 or tempF <= 13.61 or tempF <= 14.61 or tempF <= 15.61 or tempF <= 16.61 or tempF <= 17.61 or tempF <= 18.61 or tempF <= 19.61: break
            tempFE[n] = tempF

def decisao(n, estado, estadoEncomenda, locEncomenda, localizacoes, tempIE, tempFE):
    print("Deseja entregar a encomenda?" + chr(13) + "1 - Sim" + chr(13) + "2 - Não")
    while True:    #This simulates a Do Loop
        decisao = int(input())
        if decisao <= 2 and decisao >= 1: break
    if decisao == 1:
        mostraMenuEntregas(n, estado, estadoEncomenda, locEncomenda, localizacoes, tempIE, tempFE)
    else:
        print("Indique o motivo da recusa")
        motivoRecusa = input()
        estadoEncomenda[n] = estado[4]
        print(estadoEncomenda[n])

def diciEstado(estado):
    estado[0] = "criada"
    estado[1] = "emRecolha"
    estado[2] = "emDistribuicao"
    estado[3] = "entregue"
    estado[4] = "entregaRecusada"
    estado[5] = "entregaCancelada"

def diciLocs(localizacoes):
    localizacoes[0] = "norte"
    localizacoes[1] = "centro"
    localizacoes[2] = "sul"

def estadosEncomendas():
    print("Indique o estado da encomenda" + chr(13) + "1 - Em Recolha" + chr(13) + "2 - Em Distribuição" + chr(13) + "3 - Entregue")

def listaEncomendas(encomendas, numEncomendas):
    print("Lista de Encomendas")
    for i in range(1, numEncomendas + 1, 1):
        print(encomendas[i - 1])

def menuEntregas():
    print("Menu Entregas" + chr(13) + " 1 - Atualizar o estado da encomenda" + chr(13) + "2 - Reportar Anomalias" + chr(13) + "3 - Registar Localização" + chr(13) + "4 - Sair")

def metricas(estadoEncomenda, numEncomendas, numESucedidas, tempIE, tempFE):
    taxaSucesso = 0
    i = 0
    if numEncomendas == 0:
        pass
    else:
        while i <= numEncomendas:
            if estadoEncomenda[i] == "entregue":
                numESucedidas = numESucedidas + 1
            i = i + 1
        taxaSucesso = float(numESucedidas) / numEncomendas * 100
    print("Métricas Pessoais: " + chr(13) + "Entregas realizadas: " + str(numESucedidas) + chr(13) + "Taxa de Sucesso de Entregas: " + str(taxaSucesso) + "%")
    for i in range(0, numEncomendas + 1, 1):
        print("Tempo Inicial: " + str(tempIE[i]) + " Tempo Final: " + str(tempFE[i]))

def mostraMenuEntregas(n, estado, estadoEncomenda, locEncomenda, localizacoes, tempIE, tempFE):
    opcao = 1
    while opcao != 4:
        menuEntregas()
        opcao = int(input())
        if opcao == 1:
            atualizarEstado(n, estado, estadoEncomenda, tempIE, tempFE)
        else:
            if opcao == 2:
                reportarAnomalia(n, estado, estadoEncomenda)
            else:
                if opcao == 3:
                    registarLoc(n, locEncomenda, localizacoes)

def mostraMenuPrincipal():
    print("1 - Registar Encomenda " + chr(13) + "2 - Lista de Encomendas" + chr(13) + "3 - Atribuição de Encomendas" + chr(13) + "4 - Consulta de métricas Pessoais" + chr(13) + "5 - Sair")

def obtemDadosEncomenda(encomenda, numEncomendas):
    print("Digite o codigo para a encomenda " + str(numEncomendas + 1))
    while True:    #This simulates a Do Loop
        codigo = int(input())
        if codigo > 0: break
    encomenda[0] = "" + str(codigo)
    print("Digite o nome associado à encomenda")
    nome = input()
    encomenda[1] = nome
    print("Digite o seu contacto")
    while True:    #This simulates a Do Loop
        contacto = int(input())
        if contacto > 0: break
    encomenda[2] = "" + str(contacto)
    print("Digite a morada da encomenda")
    morada = input()
    encomenda[3] = morada

def obtemEncomenda(n):
    print("Indique o numero da encomenda")
    while True:    #This simulates a Do Loop
        n = int(input())
        if n > 0: break
    n = n - 1

def registaEncomenda(encomendas, encomenda, numEncomendas):
    encomendas[numEncomendas] = encomenda[0] + ";" + encomenda[1] + ";" + encomenda[2] + ";" + encomenda[3]

def registarLoc(n, locEncomenda, localizacoes):
    print("Indique a região de entrega da encomenda" + chr(13) + "1 - norte" + chr(13) + "2 - Centro" + chr(13) + "3 - Sul")
    while True:    #This simulates a Do Loop
        opcaoloc = int(input())
        if opcaoloc > 0 and opcaoloc <= 4: break
    opcaoloc = opcaoloc - 1
    locEncomenda[n] = localizacoes[opcaoloc]

def reportarAnomalia(n, estado, estadoEncomenda):
    print("Reporte a anomalia")
    anomalia = input()
    estadoEncomenda[n] = estado[5]

def zerarEstadoEncomenda(estadoEncomenda):
    for i in range(0, 99 + 1, 1):
        estadoEncomenda[i] = ""

def zerarTempos(tempIE, tempFE):
    for i in range(0, 99 + 1, 1):
        tempIE[i] = 0
    for i in range(0, 99 + 1, 1):
        tempFE[i] = 0

# Main
n = 0
encomenda = [""] * (4)

numEncomendas = 0
numESucedidas = 0
encomendas = [""] * (100)
estadoEncomenda = [""] * (100)
locEncomenda = [""] * (100)
tempIE = [0] * (100)
tempFE = [0] * (100)

zerarEstadoEncomenda(estadoEncomenda)
zerarTempos(tempIE, tempFE)
estado = [""] * (6)
localizacoes = [""] * (3)

diciLocs(localizacoes)
diciEstado(estado)
opcao = 1
while opcao != 5:
    mostraMenuPrincipal()
    opcao = int(input())
    if opcao == 1:
        obtemDadosEncomenda(encomenda, numEncomendas)
        registaEncomenda(encomendas, encomenda, numEncomendas)
        numEncomendas = numEncomendas + 1
        estadoEncomenda[numEncomendas - 1] = estado[0]
    else:
        if opcao == 2:
            listaEncomendas(encomendas, numEncomendas)
        else:
            if opcao == 3:
                obtemEncomenda(n)
                decisao(n, estado, estadoEncomenda, locEncomenda, localizacoes, tempIE, tempFE)
            else:
                if opcao == 4:
                    metricas(estadoEncomenda, numEncomendas, numESucedidas, tempIE, tempFE)
