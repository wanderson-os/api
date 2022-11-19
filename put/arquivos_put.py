import os
from resourcess.env import UPLOAD_FOLDER
from flask_restful import Resource, request


class PutFile(Resource):

  def put(self, nome):
    arquivo = request.files.get("MeuArquivo")
    arquivo_upload = ""
    for arq in os.listdir(UPLOAD_FOLDER):
      if (arq == nome):
        arquivo_upload = arq
      if arquivo_upload:
        arquivo.save(os.path.join(UPLOAD_FOLDER, arquivo_upload))
        return "<h2>Aquivo alterado com sucesso !</h2>", 200
    return "<h2>Arquivo não encontrado</h2>", 500
