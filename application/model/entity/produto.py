
class Produtos:
    
    def __init__(self, id, titulo, preco, imagem, estoque, status):
        self.__id = id
        self.__titulo = titulo
        self.__preco = preco
        self.__imagem = imagem
        self.__estoque = estoque
        self.__status = status
        
    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo

    def get_preco(self):
        return self.__preco

    def get_imagem(self):
        return self.__imagem

    def get_estoque(self):
        return self.__estoque
    
    def get_status(self):
        return self.__status
    