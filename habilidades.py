from flask_restful import Resource, request
import json

lista_habilidades = ["Python", 
                     "JavaScript", 
                     "HTML", 
                     "CSS", 
                     "FLASK", 
                     "PHP", 
                     "Java"]

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados)
        return dados
    
class AlteraOuRemoveHabilidade(Resource):
    def get(self, id):
        return lista_habilidades[id]
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados
    def delete(self, id):
        lista_habilidades.pop(id)
        return {"status":"Sucesso", "mensagem":"Habilidade excluída com sucesso!"}