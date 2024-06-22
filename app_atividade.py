from flask import Flask, jsonify, request
import json

app = Flask (__name__)

tarefas = [
    {
        "id":0,
        "responsavel": "Gabriel",
        "tarefa": "Desenvolver o método GET",
        "status": "Em andamento"
    },
    {
        "id":1,
        "responsavel": "Gabriel",
        "tarefa": "Desenvolver o método PUT",
        "status": "Concluído"
    },
     {
        "id":2,
        "responsavel": "Gabriel",
        "tarefa": "Desenvolver o método POST",
        "status": "Atrasado"
     },
     {
        "id":3,
        "responsavel": "Gabriel",
        "tarefa": "Desenvolver o método DELETE",
        "status": "A tempo"
     }
]

#Devolve uma tarefa pelo ID, também altera e deleta uma tarefa
@app.route("/tarefas/<int:id>/", methods=["GET", "PUT", "DELETE"])
def tarefa(id):
    if request.method == "GET":
        try:
            response = tarefas[id] 
        except IndexError:
            mensagem = f"Tarefa de ID {id} não existe!"
            response = {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro desconhecido!"
            response = {"status": "erro", "mensagem": mensagem}
        return jsonify (response)
    
    elif request.method == "PUT":
        dados = json.loads(request.data)
        tarefas[id]["status"] = dados
        return jsonify(dados)
    
    elif request.method == "DELETE":
        tarefas.pop(id)
        return jsonify({"status":"Sucesso", "mensagem":"Registro excluído!"})

#Lista todas as tarefas e permite registrar uma nova atividade
@app.route("/tarefas/", methods=["POST", "GET"])
def lista_tarefas():
    if request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados["id"] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
    elif request.method == "GET":
        return jsonify(tarefas)



if __name__ == "__main__":
    app.run(debug=True)
