import os
from flask import request, send_from_directory
from resourcess.env import UPLOAD_FOLDER
import zipfile
import io
import pathlib
import flask as fl
from flask_restful import Resource


class Upload_file(Resource):

  def post(self):
    arquivo = request.files.get("meuArquivo")
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(UPLOAD_FOLDER, nome_do_arquivo))
    return '<h1>Arquivo enviado com sucesso !</h1>', 200


class Dowload_files(Resource):
  def post(self):
    cont = 0
    unico_arquivo = ''
    ad = request.get_json()
    base_path = pathlib.Path(UPLOAD_FOLDER)
    data = io.BytesIO()
    lista_arquivos = ad
    with zipfile.ZipFile(data, mode='w') as z:
      for f_name in base_path.iterdir():
        for arq in lista_arquivos:
          if (f_name.name == arq['nome'] + '.' + arq['extensao']):
            z.write(f_name)
            cont = cont + 1
            unico_arquivo = arq['nome']

    data.seek(0)
    if cont > 1:
      return fl.send_from_directory(data,
                                    mimetype='application/zip',
                                    as_attachment=False,
                                    download_name='data.zip',
                                    directory=UPLOAD_FOLDER)
    else:
      if cont == 0:
        return "<h1>Nenhum arquivo encotrado ! Verifique a lista !</h1>"
      else:
        if cont == 1:
          return send_from_directory(UPLOAD_FOLDER,
                                     unico_arquivo,
                                     as_attachment=True)


class Dowload_files_Send_Link(Resource):

  def post(self):
    
    ad = request.get_json()
    base_path = pathlib.Path(UPLOAD_FOLDER)
    lista_arquivos = ad
    zip = zipfile.ZipFile("filezip.zip", 'w')
    for f_name in base_path.iterdir():
      for arq in lista_arquivos:
        if (f_name.name == arq['nome'] + '.' + arq['extensao']):
          zip.write(f_name)
    zip.close()

    return 'https://API-1.wanderson-os.repl.co/file_dowload'
  