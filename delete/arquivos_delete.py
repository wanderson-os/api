import os
from resourcess.env import UPLOAD_FOLDER
from flask_restful import Resource, request


class Delete(Resource):

  def delete(self, nome):
    arquivo_delete = ""
    for arq in os.listdir(UPLOAD_FOLDER):
      if (arq == nome):
        arquivo_delete = arq
      if arquivo_delete:
        os.remove(UPLOAD_FOLDER + "/" + nome)

        return "Aquivo removido com sucesso!", 200
    return "Arquivo não encontrado", 500
