def chr(n):
    return "\n"

def stock():
    print("Gestão de Stock")

def gestaoEncomendas():
    def adicionarMorada(c, carrinhos):
        print("Por fim digite a morada: ")
        morada = input()
        carrinhos[c] = morada
        
        return morada

    def aprovarReprovarEncomenda(encomenda, zonas, i, aprov):
        mostrarEncomendas(i, encomenda)
        while True:    #This simulates a Do Loop
            print("Qual é a encomenda que deseja verificar ?")
            numEn3 = int(input())
            numEn3 = numEn3 - 1
            if numEn3 > -1: break
        print(encomenda[numEn3])
        print("Aprovada - 1" + chr(13) + "Reprovada - 2")
        aprov1 = int(input())
        while aprov1 != 1 and aprov1 != 2:
            print("Numero invalido")
            print("Aprovada - 1" + chr(13) + "Reprovada - 2")
            aprov1 = int(input())
        if aprov1 == 1:
            aprov[numEn3] = "Aprovado"
        else:
            aprov[numEn3] = "Reprovada"

    def atribuirZona(encomenda, zonas, estafetas):
        estafeta = [""] * (5)

        estafeta[0] = "Rui Pereira / Norte"
        estafeta[1] = "Manuel Simões / Norte"
        estafeta[2] = "Andereia Gonsalves / Centro"
        estafeta[3] = "Pedro Faria / Centro"
        estafeta[4] = "Simão Moreira / Sul"
        while True:    #This simulates a Do Loop
            print("Qual é a encomenda que vai atribuir a zona e estafeta?")
            numEn2 = int(input())
            numEn2 = numEn2 - 1
            if numEn2 > -1: break
        print(encomenda[numEn2])
        print("Introduza a zona em que a morada se encontra: " + chr(13) + "Norte - 1" + chr(13) + "Centro - 2" + chr(13) + "Sul - 3")
        zona = int(input())
        while zona != 1 and zona != 2 and zona != 3:
            print("Numero invalido")
            print("Introduza a zona em que a morada se encontra: " + chr(13) + "Norte - 1" + chr(13) + "Centro - 2" + chr(13) + "Sul - 3")
            zona = int(input())
        if zona == 1:
            zonas[numEn2] = "Norte"
        else:
            if zona == 2:
                zonas[numEn2] = "Centro"
            else:
                zonas[numEn2] = "Sul"
        print("Agora introduza o estafeta" + chr(13) + "Estafetas: " + estafeta[0] + " -1" + chr(13) + estafeta[1] + " -2" + chr(13) + estafeta[2] + " -3" + chr(13) + estafeta[3] + " -4" + chr(13) + estafeta[4] + " -5")
        numEsta = int(input())
        while numEsta != 1 and numEsta != 2 and numEsta != 3 and numEsta != 4 and numEsta != 5:
            print("Numero invalido")
            print("Estafetas: " + estafeta[0] + " -1" + chr(13) + estafeta[1] + chr(13) + " -2" + estafeta[2] + chr(13) + " -3" + estafeta[3] + chr(13) + " -4" + estafeta[4] + " -5")
            numEsta = int(input())
        if numEsta == 1:
            estafetas[numEn2] = "Rui Pereira"
        else:
            if numEsta == 2:
                estafetas[numEn2] = "Manuel Simões"
            else:
                if numEsta == 3:
                    estafetas[numEn2] = "Andereia Gonsalves"
                else:
                    if numEsta == 4:
                        estafetas[numEn2] = "Pedro Faria"
                    else:
                        estafetas[numEn2] = "Simão Moreira"

    def criarCarrinho(carrinho, carrinhos, c):
        lista = 0
        while True:    #This simulates a Do Loop
            print("Qual o produto que sejá adquirir??")
            carrinho[0] = input()
            print("Agora qual a quantidade??")
            carrinho[1] = input()
            carrinhos[c] = carrinho[0] + " " + carrinho[1]
            c = c + 1
            print("Quer adicionar mais produtos a sua compra??" + chr(13) + "2 - para continuar" + chr(13) + "3 - para parar")
            pararCicloCompras = int(input())
            if pararCicloCompras == 2:
                continuarCompras = True
            else:
                continuarCompras = False
            if continuarCompras != True or c >= 10: break
        if c == 10:
            print("Maximo de produtos atingido no carrinho, finali-se a compra")
        adicionarMorada(c, carrinhos)

    def editarEncomenda(encomenda):
        while True:    #This simulates a Do Loop
            print("Qual o numeiro da encomenda ?")
            numEn = int(input())
            numEn = numEn - 1
            if numEn > -1 and numEn <= 11: break
        print(encomenda[numEn])
        print("Agora pode editar a encomenda.")
        encomenda[numEn] = input()

    def encomendas(carrinhos, c, encomenda, i):
        encomenda[i] = carrinhos[0] + " ; " + carrinhos[1] + " ; " + carrinhos[2] + " ; " + carrinhos[3] + " ; " + carrinhos[4] + " ; " + carrinhos[5] + " ; " + carrinhos[6] + " ; " + carrinhos[7] + " ; " + carrinhos[8] + " ; " + carrinhos[9] + " ; " + carrinhos[10]

    def limparArrays(zonas, encomenda, estafetas, aprov):
        for y in range(0, 10 + 1, 1):
            zonas[y] = " "
            encomenda[y] = " "
            estafetas[y] = " "
            aprov[y] = " "

    def mostrarEncomendas(i, encomenda):
        lista = 0
        while lista < i:
            print("Encomenda 1: " + encomenda[lista])
            lista = lista + 1

    def mostrarZonas(estafetas, zonas, encomenda):
        contN = 0
        print("Qual é a zona que quer procurar encomendas?")
        print("1 - Norte" + chr(13) + "2 - Centro" + chr(13) + "3 - Sul")
        numZonaEncomenda = int(input())
        while numZonaEncomenda != 1 and numZonaEncomenda != 2 and numZonaEncomenda != 3: #Verificação de input
            print("Numero invalido")
            print("1 - Norte" + chr(13) + "2 - Centro" + chr(13) + "3 - Sul")
            numZonaEncomenda = int(input())
        if numZonaEncomenda == 1: #Dar ao numero um nome
            encontrar = "Norte"
            for x in range(0, 10 + 1, 1):
                if zonas[x] == encontrar:
                    print(encomenda[x] + " ;" + " Estafeta: " + estafetas[x] + "; Zona: 5" + zonas[x])
                else:
                    contN = contN + 1
        else:
            if numZonaEncomenda == 2:
                encontrar = "Centro"
                for x in range(0, 10 + 1, 1):
                    if zonas[x] == encontrar:
                        print(encomenda[x] + " ;" + " Estafeta: " + estafetas[x] + "; Zona: " + zonas[x])
                    else:
                        contN = contN + 1
            else:
                encontrar = "Sul"
                for x in range(0, 10 + 1, 1):
                    if zonas[x] == encontrar:
                        print(encomenda[x] + " ;" + " Estafeta: " + estafetas[x] + "; Zona: " + zonas[x])
                    else:
                        contN = contN + 1
        if contN == 11:
            print("Nenhuma encomenda encontrada nessa zona")

    # Main
    carrinhos = [""] * (11)
    zonas = [""] * (11)
    carrinho = [""] * (2)
    encomenda = [""] * (11)
    estafetas = [""] * (11)
    aprov = [""] * (11)

    c = 0
    i = 0
    limparArrays(zonas, encomenda, estafetas, aprov)
    while True:    #This simulates a Do Loop
        for z in range(0, 10 + 1, 1):
            carrinhos[z] = " "
        print("Menu: " + chr(13) + "Criar encomenda - 1" + chr(13) + "Modificar encomenda - 2" + chr(13) + "Atribuir zona - 3" + chr(13) + "Aprovar ou reprovar encomendas - 4" + chr(13) + "Filtrar encomendas - 5" + "\n" + "Sair - 6")
        menu = int(input())
        if menu == 1:
            criarCarrinho(carrinho, carrinhos, c)
            encomendas(carrinhos, c, encomenda, i)
            i = i + 1
        else:
            if menu == 2:
                editarEncomenda(encomenda)
            else:
                if menu == 3:
                    atribuirZona(encomenda, zonas, estafetas)
                else:
                    if menu == 4:
                        aprovarReprovarEncomenda(encomenda, zonas, i, aprov)
                    else:
                        if menu == 5:
                            mostrarZonas(estafetas, zonas, encomenda)   
        if menu == 6: break

    
    

def estafeta():
    print("Gestão de Estafeta")
 



#Login Section

print("Login")
Username = input("Username: ")
Password = input("Password: ")
if Username == "admin" and Password == "admin":
    print("Bem-vindo ao sistema de gestão" + "\n" + "1 - Stock" + "\n" + "2 - Encomendas" + "\n" + "3 - Estafeta")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        stock()
    else:
        if opcao == 2:
            gestaoEncomendas()
        else:
            if opcao == 3:
                estafeta()
else:
    print("Bem-vindo ao nosso site")

