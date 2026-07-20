from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Hubinta xiriirka Database-ka ee Render/Supabase
database_url = os.environ.get('DATABASE_URL')
print("Halkan waa URL-ka Database-ka:", database_url)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }

with app.app_context():
    db.create_all()

@app.route('/api/items', methods=['GET'])
def get_items():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@app.route('/api/add-item', methods=['POST'])
def add_item():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    
    if not name or not price:
        return jsonify({'error': 'Fadlan geli magaca iyo qiimaha!'}), 400
        
    new_product = Product(name=name, price=float(price))
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({'message': 'Waa la keydiyay!', 'product': new_product.to_dict()})

if __name__ == '__main__':
    app.run(debug=True)
