def chr(n):
    return "\n"
def adicionarMorada(c, carrinhos):
    print("[DEBUG] Entering adicionarMorada with c=" + str(c))
    print("Por fim digite a morada: ")
    morada = input()
    carrinhos[c] = morada
    print("[DEBUG] Address added: " + morada)
    print("2")    
    return morada

def aprovarReprovarEncomenda(encomenda, zonas, i, aprov):
    print("[DEBUG] Entering aprovarReprovarEncomenda with i=" + str(i))
    mostrarEncomendas(i, encomenda)
    while True:    #This simulates a Do Loop
        print("Qual é a encomenda que deseja verificar ?")
        numEn3 = int(input())
        numEn3 = numEn3 - 1
        print("[DEBUG] Selected package index: " + str(numEn3))
        if numEn3 > -1: break
    print(encomenda[numEn3])
    print("Aprovada - 1" + chr(13) + "Reprovada - 2")
    aprov1 = int(input())
    print("[DEBUG] Approval choice: " + str(aprov1))
    while aprov1 != 1 and aprov1 != 2:
        print("Numero invalido")
        print("Aprovada - 1" + chr(13) + "Reprovada - 2")
        aprov1 = int(input())
    if aprov1 == 1:
        aprov[numEn3] = "Aprovado"
        print("[DEBUG] Package approved")
    else:
        aprov[numEn3] = "Reprovada"
        print("[DEBUG] Package rejected")

def atribuirZona(encomenda, zonas, estafetas):
    print("[DEBUG] Entering atribuirZona")
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
        print("[DEBUG] Selected package: " + str(numEn2))
        if numEn2 > -1: break
    print(encomenda[numEn2])
    print("Introduza a zona em que a morada se encontra: " + chr(13) + "Norte - 1" + chr(13) + "Centro - 2" + chr(13) + "Sul - 3")
    zona = int(input())
    print("[DEBUG] Zone selected: " + str(zona))
    while zona != 1 and zona != 2 and zona != 3:
        print("Numero invalido")
        print("Introduza a zona em que a morada se encontra: " + chr(13) + "Norte - 1" + chr(13) + "Centro - 2" + chr(13) + "Sul - 3")
        zona = int(input())
    if zona == 1:
        zonas[numEn2] = "Norte"
        print("[DEBUG] Zone set to: Norte")
    else:
        if zona == 2:
            zonas[numEn2] = "Centro"
            print("[DEBUG] Zone set to: Centro")
        else:
            zonas[numEn2] = "Sul"
            print("[DEBUG] Zone set to: Sul")
    print("Agora introduza o estafeta" + chr(13) + "Estafetas: " + estafeta[0] + " -1" + chr(13) + estafeta[1] + " -2" + chr(13) + estafeta[2] + " -3" + chr(13) + estafeta[3] + " -4" + chr(13) + estafeta[4] + " -5")
    numEsta = int(input())
    print("[DEBUG] Courier selected: " + str(numEsta))
    while numEsta != 1 and numEsta != 2 and numEsta != 3 and numEsta != 4 and numEsta != 5:
        print("Numero invalido")
        print("Estafetas: " + estafeta[0] + " -1" + chr(13) + estafeta[1] + chr(13) + " -2" + estafeta[2] + chr(13) + " -3" + estafeta[3] + chr(13) + " -4" + estafeta[4] + " -5")
        numEsta = int(input())
    if numEsta == 1:
        estafetas[numEn2] = "Rui Pereira"
        print("[DEBUG] Courier set to: Rui Pereira")
    else:
        if numEsta == 2:
            estafetas[numEn2] = "Manuel Simões"
            print("[DEBUG] Courier set to: Manuel Simões")
        else:
            if numEsta == 3:
                estafetas[numEn2] = "Andereia Gonsalves"
                print("[DEBUG] Courier set to: Andereia Gonsalves")
            else:
                if numEsta == 4:
                    estafetas[numEn2] = "Pedro Faria"
                    print("[DEBUG] Courier set to: Pedro Faria")
                else:
                    estafetas[numEn2] = "Simão Moreira"
                    print("[DEBUG] Courier set to: Simão Moreira")

def criarCarrinho(carrinho, carrinhos, c):
    print("[DEBUG] Entering criarCarrinho with c=" + str(c))
    lista = 0
    while True:    #This simulates a Do Loop
        print("Qual o produto que sejá adquirir??")
        carrinho[0] = input()
        print("Agora qual a quantidade??")
        carrinho[1] = input()
        carrinhos[c] = carrinho[0] + " " + carrinho[1]
        print("[DEBUG] Product added - Item: " + carrinho[0] + ", Quantity: " + carrinho[1])
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
    print("[DEBUG] Cart creation complete with " + str(c) + " items")
    adicionarMorada(c, carrinhos)

def editarEncomenda(encomenda):
    print("[DEBUG] Entering editarEncomenda")
    while True:    #This simulates a Do Loop
        print("Qual o numeiro da encomenda ?")
        numEn = int(input())
        numEn = numEn - 1
        print("[DEBUG] Package index selected: " + str(numEn))
        if numEn > -1 and numEn <= 11: break
    print(encomenda[numEn])
    print("Agora pode editar a encomenda.")
    encomenda[numEn] = input()
    print("[DEBUG] Package updated")

def encomendas(carrinhos, c, encomenda, i):
    print("[DEBUG] Creating package at index " + str(i))
    encomenda[i] = carrinhos[0] + " ; " + carrinhos[1] + " ; " + carrinhos[2] + " ; " + carrinhos[3] + " ; " + carrinhos[4] + " ; " + carrinhos[5] + " ; " + carrinhos[6] + " ; " + carrinhos[7] + " ; " + carrinhos[8] + " ; " + carrinhos[9] + " ; " + carrinhos[10]
    print("[DEBUG] Package created: " + encomenda[i])

def limparArrays(zonas, encomenda, estafetas, aprov):
    for y in range(0, 10 + 1, 1):
        zonas[y] = " "
        encomenda[y] = " "
        estafetas[y] = " "
        aprov[y] = " "

def mostrarEncomendas(i, encomenda):
    print("[DEBUG] Displaying " + str(i) + " packages")
    lista = 0
    while lista < i:
        print("Encomenda 1: " + encomenda[lista])
        lista = lista + 1

def mostrarZonas(estafetas, zonas, encomenda):
    print("[DEBUG] Entering mostrarZonas")
    contN = 0
    print("Qual é a zona que quer procurar encomendas?")
    print("1 - Norte" + chr(13) + "2 - Centro" + chr(13) + "3 - Sul")
    numZonaEncomenda = int(input())
    print("[DEBUG] Zone search selected: " + str(numZonaEncomenda))
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
print("[DEBUG] Main program initialized")
limparArrays(zonas, encomenda, estafetas, aprov)
while True:    #This simulates a Do Loop
    for z in range(0, 10 + 1, 1):
        carrinhos[z] = " "
    print("Menu: " + chr(13) + "Criar encomenda - 1" + chr(13) + "Modificar encomenda - 2" + chr(13) + "Atribuir zona - 3" + chr(13) + "Aprovar ou reprovar encomendas - 4" + chr(13) + "Filtrar encomendas - 5" + "\n" + "Sair - 6")
    menu = int(input())
    print("[DEBUG] Menu choice: " + str(menu))
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
    if menu == 6:
        print("[DEBUG] Exiting program")
        break
