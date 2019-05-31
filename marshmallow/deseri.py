from marshmallow import Schema, fields


class BookSchema(Schema):
	title = fields.Str()
	author = fields.Str()

data = {
	"title": "Something",
	"author": "boi",
	"description": "feels"
}

book_schema = BookSchema()
book = book_schema.load(data)

print(book)
