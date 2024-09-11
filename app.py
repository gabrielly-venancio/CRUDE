from flask import Flask,jsonify
import user

app = Flask(__name__)

@app.route('/api/getUser', methods=['GET'])
def getUser():
    dados = user.users
    usuarios = jsonify(dados['user'])
    return usuarios

if __name__ == '__main__':
    app.run(debug = True)