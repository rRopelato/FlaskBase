from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

class Clients(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    address = db.Column(db.String(255))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/clients')
def get_clients():
    clients = Clients.query.all()
    data = [
        {
            "id": client.id,
            "first_name": client.first_name,
            "last_name": client.last_name,
            "email": client.email,
            "phone": client.phone,
            "address": client.address,
        }
        for client in clients
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='192.0.0.0', port=5000)