from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.shopping
## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/order', methods=['POST'])
def test_post():
    name_received=request.form['name_give']
    count_received=int(request.form['count_give'])
    address_received=request.form['address_give']
    phone_received=request.form['phone_give']
    item_received=request.form['item_give']

    orderInfo={
        'name': name_received,
        'count':count_received,
        'address': address_received,
        'phone':phone_received,
        'item':item_received
    }
    db.shopping.insert_one(orderInfo)

    print(name_received,count_received,address_received,phone_received,item_received)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

@app.route('/order',methods=['GET'])
def test_get():

    item_received=request.args.get('item_give')

    result = list( db.shopping.find({'item':item_received},{'_id':0}))

    print(result)
    return jsonify({'result': 'success', 'info': result})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5300,debug=True)
