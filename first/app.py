from flask import Flask, jsonify

app = Flask(__name__)

stores = [
	{
		'name': 'Tianguis',
		'items': [
			{
				'name': 'Mona china',
				'price': 500
			}
		]
	}
]

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
   pass

# GET /store/<string:name>
@app.route('/stote/<string:name>') 
def get_store(name):
   pass

# GET /store
@app.route('/store')
def get_stores():
   return jsonify({'stores': stores}) 

# POST /store/<string:name>/item {name:, price}
@app.route('/stotr/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
   pass 

# GET /store/<string:name>/item
@app.route('/route/<string:name>/item')
def get_items_in_store(name):
   pass





app.run(port=5000)
