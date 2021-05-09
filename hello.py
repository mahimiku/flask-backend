from flask import Flask
from flask_cors import CORS
import json
from flask_mysqldb import MySQL
 
app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = '117.239.163.143'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '402@flatAB'
app.config['MYSQL_DB'] = 'practice_db'

# app.config['MYSQL_PASSWORD'] = '12345'
# app.config['MYSQL_DB'] = 'mobile_store'

mysql = MySQL(app)


@app.route('/hello')
def hello_world():

        cursor = mysql.connection.cursor()

        rawquery = f"select * from flatmate where id = 1"
        # rawquery = f"select id, name, email from users where id = 1"

        cursor.execute(rawquery)
        result = cursor.fetchone()
        print(result)

        data = {}
        data['success'] = True
        # data['msg'] = "Hello Mr. Mahipal Singh, Bhai balcony ka gate open rakha kr"
        data['msg'] = result
        return json.dumps(data), 200, {'content-type': 'application/json'}

if __name__ == '__main__':
        app.debug = True
        app.run(host='0.0.0.0', port=5000, debug=True)
