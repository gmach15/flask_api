from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades, AlteraOuRemoveHabilidade

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        "id":0,
        "nome": "Gabriel",
        "habilidades": ["Python", "Flask"]
    },
    {
        "id":1,
        "nome": "José",
        "habilidades": ["C#", "Spring Boot"]
    },
     {
        "id":2,
        "nome": "Aurélio",
        "habilidades": ["Java", "Spring Boot", "Swagger"]
     }
]

#Devolve um Dev pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        if request.method == "GET":
            try:
                response = desenvolvedores[id] 
            except IndexError:
                mensagem = f"Desenvolvedor de ID {id} não existe!"
                response = {"status": "erro", "mensagem": mensagem}
            except Exception:
                mensagem = "Erro desconhecido!"
                response = {"status": "erro", "mensagem": mensagem}
            return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status":"Sucesso", "mensagem":"Registro excluído!"}

#Lista todos os Dev e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
      
api.add_resource(Desenvolvedor, "/dev/<int:id>/") 
api.add_resource(ListaDesenvolvedores, "/dev/")
api.add_resource(Habilidades, "/habilidades/")
api.add_resource(AlteraOuRemoveHabilidade, "/habilidades/<int:id>/")

if __name__ == "__main__":
    app.run()