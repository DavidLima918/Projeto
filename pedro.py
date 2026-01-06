def chr(n):
    return "\n"

def avaliarServico(estadoPedido, totalPedidos):
    print("Deseja avaliar qual pedido?")
    totalPedidos = int(input())
    if estadoPedido[totalPedidos - 1] == "estado concluído":
        print("Poderia dar uma nota para avaliar o serviço que foi prestado? (Rating 1-5)")
        while True:    #This simulates a Do Loop
            rating = int(input())
            if rating > 5 and rating < 0: break
            print("A nota que o utilizador atribuiu não está disponível. Tente novamente de 1 a 5.")
            rating = int(input())
        print("Poderia colocar um comentário ao serviço?")
        comentario = input()
        print("Obrigado!")
    else:
        print("O seu pedido ainda não foi concluído!")

def criarPedido(pedidos, elementosPedidos, totalPedidos, estadoPedido):
    print("Para começar deve escrever qual é a origem do pedido:")
    elementosPedidos[0] = input()
    print("Agora, introduza o destino do pedido.")
    elementosPedidos[1] = input()
    print("Introduza a sua janela temporal para receber a sua encomenda:")
    elementosPedidos[2] = input()
    print("Por fim, deve introduzir a descrição com os itens do seu pedido.")
    elementosPedidos[3] = input()
    if elementosPedidos[0] != "" and elementosPedidos[1] != "" and elementosPedidos[2] != "" and elementosPedidos[3] != "":
        print("O seu pedido foi criado.")
        print("Com o pedido criado, deve informar qual é a data do pedido.(Formato DD/MM/AAAA)")
        elementosPedidos[4] = input()
        while elementosPedidos[4] == "":
            print("A data do pedido é obrigatória! Deve voltar a escrever a data!")
            elementosPedidos[4] = input()
        elementosPedidos[5] = "estado pendente"
        estadoPedido[totalPedidos] = elementosPedidos[5]
        print("Obrigado! O seu pedido encontra-se no estado pendente!")
        pedidos[totalPedidos] = elementosPedidos[0] + ";" + elementosPedidos[1] + ";" + elementosPedidos[2] + ";" + elementosPedidos[3] + ";" + elementosPedidos[4] + ";" + elementosPedidos[5]
    else:
        print("O seu pedido não foi criado. Algum dos dados obrigatórios não foi corretamente preenchido, com isso, deve recomeçar o seu novo pedido.")
        pedidos[totalPedidos] = ""

def estadoPedido(elementosPedidos, totalPedidos, estadoPedido):
    estadoPedido[totalPedidos - 1] = elementosPedidos[5]

def trackingBasico(estadoPedido, totalPedidos):
    print("Deseja ver o Tracking Básico de qual pedido?")
    totalPedidos = int(input())
    totalPedidos = totalPedidos - 1
    if estadoPedido[totalPedidos] == "estado pendente":
        print("O pedido encontra-se no estado pendente. Analisando os últimos detalhes.")
        estadoPedido[totalPedidos] = "estado enviado"
        print("O seu pedido já foi enviado!")
        estadoPedido[totalPedidos] = "estado entregue"
        print("O seu pedido já foi entregue!")
        estadoPedido[totalPedidos] = "estado concluído"
        print("O seu pedido encontra-se finalizado!")
    else:
        if estadoPedido[totalPedidos - 1] == "estado enviado":
            print("O seu pedido já foi enviado. Aguarde pela entrega!")
            estadoPedido[totalPedidos] = "estado entregue"
            print("O seu pedido já foi entregue!")
            estadoPedido[totalPedidos] = "estado concluído"
            print("O seu pedido encontra-se finalizado!")
        else:
            if estadoPedido[totalPedidos - 1] == "entregue":
                estadoPedido[totalPedidos] = "estado concluído"
                print("O pedido já foi entregue. Encontra-se finalizado!")

def verPedidos(pedidos, totalPedidos):
    print("Qual é o pedido que deseja ver?")
    totalPedidos = int(input())
    print(pedidos[totalPedidos - 1])

# Main
nome = [""] * (10)
estadoPedido = [""] * (10)
pedidos = [""] * (10)
elementosPedidos = [""] * (6)

totalPedidos = 0
print("Olá, Bem-vindo! Para começar deve digitar o seu o nome da cliente.")
nome[totalPedidos] = input()
while True:    #This simulates a Do Loop
    print("Menu:" + chr(13) + "1-Criar Pedidos" + chr(13) + "2-Ver Pedidos" + chr(13) + "3-Tracking Básico" + chr(13) + "4-Avaliar Serviço" + chr(13) + "0-Sair")
    a = int(input())
    if a == 1:
        criarPedido(pedidos, elementosPedidos, totalPedidos, estadoPedido)
        totalPedidos = totalPedidos + 1
    else:
        if a == 2:
            verPedidos(pedidos, totalPedidos)
        else:
            if a == 3:
                trackingBasico(estadoPedido, totalPedidos)
            else:
                if a == 4:
                    avaliarServico(estadoPedido, totalPedidos)
    if a == 0: break

