from flask import Flask, jsonify,json, request

app = Flask(__name__)
with open ('stores.json', 'r') as infile:
	stores = json.load(infile)
	stores = json.loads(stores)


#post - receive data
#get - send data

# POST /store data: {name:}
@app.route('/store', methods=['POST'])#endpoint, default is a get request
def create_store():
	request_data = request.get_json() # request made to this endpoint. 
	new_store = {
		'name' : request_data['name'],
		'items' : []
	}
	stores.append(new_store)
	with open('test.json', 'w') as outfile:
		json.dump(stores,outfile)
	return jsonify(new_store)

#get /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
	#iterate over stores
	for i in range(0,len(stores)):
		if stores[i]['name'] == name:
			return jsonify(stores[i])
		#else:
		#	return "Sorry no store found with name: {}".format(name)
	return jsonify({'message': 'store: '+name+' not found'})

#get /store
@app.route('/store')
def get_stores():
	output = []
	for i in range (0,len(stores)):
		output.append(stores[i]["name"])
	return jsonify(output)

	#return jsonify({'stores' : stores[1]})
	
	#POST/store/name/item name, price
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
	request_data = request.get_json()
	new_item = {
	'name' : request_data['name'],
	'price': request_data['price']}
	for store in stores:
		if store['name'] == name:
			store['items'].append(new_item)
			return jsonify({'items' : store['items']})
	return jsonify({'message' : 'Sorry, can\'t create item in an unknown store.'})

#get /store/string:name/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
	for i in range(0,len(stores)):
		if stores[i]['name'] == name:
			return jsonify({'items' : stores[i]['items']})
	return jsonify({'message' : 'No items foun in store: '+name+' .'})

app.run()