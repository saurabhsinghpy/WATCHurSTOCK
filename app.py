from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from database import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Watchlist

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    new_user = User(email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/add_watchlist', methods=['POST'])
@jwt_required()
def add_watchlist():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_stock = Watchlist(user_id=user_id, stock_symbol=data['symbol'], alert_price=data['price'])
    db.session.add(new_stock)
    db.session.commit()
    return jsonify({"message": "Stock added to watchlist"}), 201

if __name__ == '__main__':
    app.run(debug=True)

