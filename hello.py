from flask import Flask
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello_world():
        data = {}
        data['success'] = True
        data['msg'] = "Hello Mr. Amit Singh, Kab shaadi kijiyega?"
        return json.dumps(data), 200, {'content-type': 'application/json'}

if __name__ == '__main__':
        app.debug = True
        app.run(host='0.0.0.0', port=5000, debug=True)
