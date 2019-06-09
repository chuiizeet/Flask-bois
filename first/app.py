from flask import Flask

app = Flask(__name__)

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
   pass

# GET /store/<string:name>
@app.route('/stote/<string:name>', methods=['GET', 'POST'])
def method_name():
   pass





app.run(port=5000)
