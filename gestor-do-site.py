produtos = {
    "Assinatura Mensal": 24.99,
    "Assinatura Anual": 12 * 19.99,
    "Assinatura Premium": 45.99
}

def cadastrar_produto():
    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    produtos[nome] = preco
    print("Produto cadastrado com sucesso!\n")

def listar_produtos():
    print("Produtos cadastrados:\n")
    for nome, preco in produtos.items():
        print(f"{nome}: R$ {preco:.2f}")
    print()

def buscar_produto():
    nome = input("Informe o nome do produto que deseja buscar: ")
    if nome in produtos:
        preco = produtos[nome]
        print(f"{nome}: R$ {preco:.2f}\n")
    else:
        print("Produto não encontrado.\n")

def remover_produto():
    nome = input("Informe o nome do produto que deseja remover: ")
    if nome in produtos:
        del produtos[nome]
        print("Produto removido com sucesso!\n")
    else:
        print("Produto não encontrado.\n")

while True:
    print("Bem-vindo ao programa de gestão de produtos!\n")
    print("Escolha uma opção:\n")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Buscar produto")
    print("4. Remover produto")
    print("5. Sair\n")
    
    opcao = input("Digite a opção desejada: ")
    print()

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        buscar_produto()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        print("Obrigado por utilizar o programa de gestão de produtos!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")