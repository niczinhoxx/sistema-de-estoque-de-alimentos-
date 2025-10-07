## SISTEME DE VERIFICAÇÃO DE ALGUNS  ESTOQUES
alimento1 = "carne"
alimento2 = "frutas"
alimento3 = "sucos"
alimento4 = "biscoitos"

## DANDO AS OPÇÕES PARA O USUÁRIO ESCOLHER
print("Digite 1 para inserir e acessar o estoque de Carnes:")
print("Digite 2 para inserir e acessar o estoque de Frutas:")
print("Digite 3 para inserir e acessar o estoque de Sucos:")
print("Digite 4 para inserir e acessar o estoque de Biscoitos:")

## RECEBENDO A OPÇÃO QUE ELE ESCOLHEU
opcao = int(input("Qual das opções você deseja acessar? "))

## FUNÇÃO PARA ARMAZENAR OS DADOS RECEBIDOS
def sistema_estoque(opcao):
    match opcao:
        case 1:
            print("Insira o estoque da Carne:")
            carne1 = int(input("Quantidade: "))
            if carne1 >= 70:
                print("Carne dentro do nível requerido")
            else:
                print("Carne fora do nível requerido")

        case 2:
            print("Insira o estoque de Frutas:")
            frutas = int(input("Quantidade: "))
            if frutas >= 50:
                print("Frutas dentro do nível requerido")
            else:
                print("Frutas fora do nível requerido")

        case 3:
            print("Insira o estoque de Sucos:")
            sucos = int(input("Quantidade: "))
            if sucos >= 30:
                print("Sucos dentro do nível requerido")
            else:
                print("Sucos fora do nível requerido")

        case 4:
            print("Insira o estoque de Biscoitos:")
            biscoitos = int(input("Quantidade: "))
            if biscoitos >= 40:
                print("Biscoitos dentro do nível requerido")
            else:
                print("Biscoitos fora do nível requerido")

        case _:
            print("Opção inválida. Tente novamente.")

# Chama a função
sistema_estoque(opcao)
