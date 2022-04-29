
from application.model.entity.produto import Produtos
class ProdutoDao:

    def listar_produto():
        #Retorar uma lista de produtos!
        lista_produtos = [
        Produtos(id=1,titulo="Televisao 58",preco=2500,imagem= "3.png", estoque=20,status=1),
        Produtos(id=2,titulo="Televisao 42",preco=1800,imagem= "3.png",estoque=30,status=1),
        Produtos(id=3,titulo="Televisao 32",preco=1300,imagem= "3.png",estoque=20,status=1)
        ]
        return lista_produtos

