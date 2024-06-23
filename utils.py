from models import Pessoas, Usuarios

#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome="Letícia", idade=28)
    print(pessoa)
    pessoa.save()

#Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Robson").first()
    pessoa.nome = "Cristina"
    pessoa.save()

#Exclui um registro na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Letícia").first()
    pessoa.delete()

#consulta registros da tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome="Gabriel").first()
    print(pessoas)

#Insere um usuário na tabela Usuários
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == "__main__":
    #insere_usuario("Gabriel", int("654321"))
    #insere_usuario("Yasmin", int("123456"))
    #consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
