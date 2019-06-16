import sqlite3
from flask_restful import Resource, reqparse, request
from flask_jwt import jwt_required

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
		type=float,
		required=True,	
		help="This field cannot be left blank!"
	)

	@classmethod
	def find_by_name(cls, name):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM items WHERE name=?"
		result = cursor.execute(query, (name,))
		row = result.fetchone()
		connection.close

		if row:
			return {'item': {'name': row[0], 'price': row[1]}}

	@jwt_required()
	def get(self, name):
		item = self.find_by_name(name)
		if item:
			return item
		else:
			return {'message': 'Item not found'}, 404

	def post(self, name):
		if self.find_by_name(name):
			return {'message': "An item with name '{}' already exists. ".format(name)}, 400

		data = request.get_json()
		item = {'name': name, 'price': data['price']}

		try:
			self.insert(item)
		except:
			return {'message': 'An error ocurred inserting the item.'}, 500
		

		return item, 201

	@classmethod
	def insert(cls. item):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "INSERT INTO items VALUES (?, ?)"
		cursor.execute(query, (item['name'], item['price']))

		connection.commit()
		connection.close()

	def delete(self, name):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "DELETE FROM items WHERE name=?"
		cursor.execute(query, (name,))

		connection.commit()
		connection.close()

	def put(self, name):
		data = parser.parse_args()
		item = self.find_by_name(name)

		update_item = {'name': name, 'price': data['price']}

		if item is None:
			self.insert(update_item)
		else:
			self.insert(update_item)
		return update_item

	@classmethod
	def insert(cls, item):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "UPDATE items SET price=? WHERE name=?"
		cursor.execute(query, (item['price'], item['name']))

		connection.commit()
		connection.close()


class ItemList(Resource):
	def get(self):
		return {'items': items}
