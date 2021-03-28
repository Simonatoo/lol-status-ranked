from flask import Flask,request
from controls.default import Default
import json
import re

CON = Default()
app = Flask(__name__)

@app.route(rule='/status',methods=['GET'])
def status():
    player = request.args.get('player')
    return json.dumps(CON.status(re.sub('\s','+',player)))

if __name__ == '__main__':
    app.run(port=8080,debug=True)