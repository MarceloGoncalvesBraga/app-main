from flask import render_template
from application import main
from application.model.dao.produto_dao import ProdutoDao

@main.route("/produtos")
def lista_produto():
    #Importar e instanciar o produto dao
    #Solicitar que o produto dao liste os produtos
    #Exibir na view os produtos listados
    # lista_produtos =ProdutoDao

    return render_template("produtos.html",
    produtos = ProdutoDao.listar_produto()       
                           
    )