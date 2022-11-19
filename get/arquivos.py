import os
from flask import json
from resourcess.env import UPLOAD_FOLDER, DELETE_PATH
import zipfile
import io
import pathlib
import flask as fl
from flask_restful import Resource, request

api = fl.Flask(__name__)
global cont
cont = 0


class Listar(Resource):

  def get(self):
    arquivos = []
    for nome_do_arquivo in os.listdir(UPLOAD_FOLDER):
      endereco_do_arquivo = os.path.join(UPLOAD_FOLDER, nome_do_arquivo)
      if (os.path.isfile(endereco_do_arquivo)):
        arquivos.append({'nome': nome_do_arquivo})
        response = api.response_class(response=json.dumps(arquivos),
                                      mimetype='application/json')
    return (response)


class Home(Resource):

  def get(self):
    arquivos = []
    for nome_do_arquivo in os.listdir(UPLOAD_FOLDER):
      arquivos.append({'nome': nome_do_arquivo})
      response = api.response_class(response=json.dumps(arquivos),
                                    mimetype='application/json')
    return (response)


class Download_all(Resource):

  def get(self):
    cont = 0
    base_path = pathlib.Path(UPLOAD_FOLDER)
    data = io.BytesIO()
    with zipfile.ZipFile(
        data,
        mode='w',
    ) as z:
      for f_name in base_path.iterdir():
        z.write(f_name)
        cont = cont + 1

    data.seek(0)
    if cont > 0:

      return fl.send_file(data,
                          mimetype='application/zip',
                          as_attachment=True,
                          download_name='data.zip')
    else:
      return "<h2>Sem aquivos!</h2>"


class Download_files_get(Resource):

  def get(self):
    arq = fl.send_from_directory(DELETE_PATH,
                                 "filezip.zip",
                                 as_attachment=True)
    os.remove(DELETE_PATH + "/" + "filezip.zip")
    return arq
