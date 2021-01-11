
# @author --- IT16521544 B D K Samaraweera

from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
#from compress import processCompressing
#from main import processPSD
#from resize import processResizing
from werkzeug.utils import secure_filename
import os
import json

from compress import processCompressing
from main import processPSD
from resize import processResizing
from SupunComponent import Supun_LayerIdentifier

UPLOAD_FOLDER = 'static/'

app = Flask(__name__,static_url_path='/static')
cors = CORS(app)
app.config['CORS_HEADERS'] = '*'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/images/mobile', methods = ['GET'])
@cross_origin()
def process1():
    imagelist=os.listdir("static/mobile")
    return json.dumps(imagelist)


@app.route('/images/tab', methods = ['GET'])
@cross_origin()
def process2():
    imagelist=os.listdir("static/tab")
    return json.dumps(imagelist)


@app.route('/images', methods = ['GET'])
@cross_origin()
def process3():
    imagelist = os.listdir("static/Compressed_Images")
    return json.dumps(imagelist)



@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':

      f = request.files['file']
      f.save(secure_filename(f.filename))
      processPSD(f.filename)
      processCompressing()
      processResizing()
      return 'processing done'



@app.route('/updateimage', methods = ['PUT'])
@cross_origin()
def process4():
    if request.method == 'PUT':
        replacefilename = request.args.get('replacefilename')
        f = request.files['file']
        f.save("static/mobile/"+secure_filename(replacefilename+"."+f.filename.split('.')[1]))
        return "done"

@app.route('/generateHTML', methods = ['GET'])
@cross_origin()
def process5():
    if request.method == 'GET':
        Supun_LayerIdentifier()
        return "Done"



if __name__ == '__main__':
   app.run()