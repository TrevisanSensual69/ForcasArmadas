from flask import Flask, render_template, request, redirect

class cadmilitar:
    def __init__(self, idmilitar, patente, codigo, ramo, nipatente, descricao):
        self.idmilitar = idmilitar
        self.patente = patente
        self.codigo = (codigo)
        self.ramo = (ramo)
        self.nipatente = nipatente
        self.descricao = descricao

lista = []

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Cadastro das Forças Armadas'

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo='Cadastro das Forças Armadas')

@app.route('/criar', methods=['POST'])
def criar():
    idmilitar = request.form["ID-Militares"]
    patente = request.form["patente"]
    codigo = request.form["codigo"]
    ramo = request.form["ramo"]
    nipatente = request.form["nipatente"]
    descricao = request.form["descricao"]
    obj = cadmilitar(idmilitar, patente, codigo, ramo, nipatente, descricao)
    lista.append(obj)
    return redirect('/militar')

@app.route('/militar')
def militar():
    return render_template('militar.html', Titulo="Militares", ListaMilitares = lista )

@app.route('/excluir/<IDest>', methods=['GET','DELETE'])
def militarexcluir(IDest):
    for i, militar in enumerate(lista):
        if militar.idmilitar == IDest:
            lista.pop(i)
            break
    return redirect('/militar')

@app.route('/editar/<IDest>', methods=['GET'])
def editar(IDest):
    for i, militar in enumerate(lista):
        if militar.idmilitar == IDest:
            return render_template('Editar.html', Titulo='Editar Militar', Militaresedit=militar )

@app.route('/alterar', methods=['POST', 'PUT'])
def alterar():
    id = request.form['ID-Militares']
    for i, militar in enumerate(lista):
        if militar.idmilitar == id:
            militar.patente = request.form['patente']
            militar.codigo = request.form['codigo']
            militar.ramo = request.form['ramo']
            militar.nipatente = request.form['nipatente']
            militar.descricao = request.form['descricao']
        return redirect('/militar')

if __name__ == '__main__':
    app.run()
