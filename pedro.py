def chr(n):
    return "\n"

def avaliarServico(estadoPedido, totalPedidos):
    if estadoPedido[totalPedidos] == "estado concluído":
        print("Poderia dar uma nota para avaliar o serviço que foi prestado? (Rating 1-5)")
        rating = int(input())
        while rating < 0 and rating > 6:
            print("A nota que o utilizador atribuiu não está disponível. Tente novamente de 1 a 5.")
            rating = int(input())
        print("Poderia colocar um comentário ao serviço?")
        comentario = input()
        print("Obrigado!")
    else:
        print("O seu pedido ainda não foi concluído!")

def criarPedido(pedidos, elementosPedidos, totalPedidos):
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
        print("Com o pedido criado, deve informar qual é a data do pedido;")
        elementosPedidos[4] = input()
        while elementosPedidos[4] == "":
            print("A data do pedido é obrigatória! Deve voltar a escrever a data!")
            elementosPedidos[4] = input()
        elementosPedidos[5] = "estado pendente"
        print("Obrigado! O seu pedido encontra-se no estado pendente!")
        pedidos[totalPedidos] = elementosPedidos[0] + ";" + elementosPedidos[1] + ";" + elementosPedidos[2] + ";" + elementosPedidos[3] + ";" + elementosPedidos[4] + ";" + elementosPedidos[5]
    else:
        print("O seu pedido não foi criado. Algum dos dados obrigatórios não foi corretamente preenchido, com isso, deve recomeçar o seu novo pedido.")
        pedidos[totalPedidos] = ""

def estadoPedido(elementosPedidos, totalPedidos, estadoPedido):
    estadoPedido[totalPedidos] = elementosPedidos[5]

def trackingBasico(estadoPedido, totalPedidos):
    if estadoPedido[totalPedidos] == "estado pendente":
        print("O pedido encontra-se no estado pendente. Analisando os últimos detalhes.")
        estadoPedido[totalPedidos] = "estado enviado"
        print("O seu pedido já foi enviado!")
        estadoPedido[totalPedidos] = "estado entregue"
        print("O seu pedido já foi entregue!")
        estadoPedido[totalPedidos] = "estado concluído"
        print("O seu pedido encontra-se finalizado!")
    else:
        if estadoPedido == "estado enviado":
            print("O seu pedido já foi enviado. Aguarde pela entrega!")
            estadoPedido[totalPedidos] = "estado entregue"
            print("O seu pedido já foi entregue!")
            estadoPedido[totalPedidos] = "estado concluído"
            print("O seu pedido encontra-se finalizado!")
        else:
            if estadoPedido == "entregue":
                estadoPedido[totalPedidos] = "estado concluído"
                print("O pedido já foi entregue. Encontra-se finalizado!")

# Main
nome = [""] * (10)
estadoPedido = [""] * (10)
pedidos = [""] * (10)
elementosPedidos = [""] * (6)

totalPedidos = 0
print("Olá, Bem-vindo! Para começar deve digitar o seu o nome da cliente.")
nome[totalPedidos] = input()
print("O cliente " + nome[totalPedidos] + " pretende criar um novo pedido? (s/n)")
opcao1 = input()
if opcao1 == "s":
    print("Vamos começar a criar o seu novo pedido!")
    criarPedido(pedidos, elementosPedidos, totalPedidos)
    if pedidos[totalPedidos] == "":
        print("Deve criar novamente o pedido!")
    else:
        estadoPedido(elementosPedidos, totalPedidos, estadoPedido)
        print("Pretende ver o tracking básico do seu pedido? (s/n)")
        opcao2 = input()
        if opcao2 == "s":
            trackingBasico(estadoPedido, totalPedidos)
            print("Pretende avaliar o serviço prestado? (s/n)")
            opcao3 = input()
            if opcao3 == "s":
                avaliarServico(estadoPedido, totalPedidos)
