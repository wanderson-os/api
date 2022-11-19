from get.arquivos import Download_all, Listar, Download_files_get,Home
from post.arquivos_post import Dowload_files, Upload_file, Dowload_files_Send_Link
from put.arquivos_put import PutFile
from delete.arquivos_delete import Delete
from flask_cors import CORS
import flask as fl
from flask_restful import Api

api = fl.Flask(__name__)
CORS(api)
app = Api(api)

app.add_resource(Home, '/')
app.add_resource(Listar, '/listar')
app.add_resource(Download_all, '/download_all')
app.add_resource(Dowload_files, '/download_files')
app.add_resource(Upload_file, '/upload_file')
app.add_resource(Download_files_get, '/file_dowload')
app.add_resource(Dowload_files_Send_Link, "/file_zip")
app.add_resource(PutFile, "/put_file/<string:nome>")
app.add_resource(Delete, "/delete/<string:nome>")

if __name__ == "__main__":
  api.run(host='0.0.0.0', port=3000)
