from flask import Flask, request, jsonify
import json

app = Flask(__name__)

subscriptions = []

@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    return jsonify(subscriptions)

@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    data = request.get_json()
    subscription = {
        'id': len(subscriptions) + 1,
        'phone_number': data['phone_number'],
        'plan': data['plan'],
        'status': 'active'
    }
    subscriptions.append(subscription)
    return jsonify(subscription), 201

@app.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    for subscription in subscriptions:
        if subscription['id'] == subscription_id:
            return jsonify(subscription)
    return 'Subscription not found', 404

@app.route('/subscriptions/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    data = request.get_json()
    for subscription in subscriptions:
        if subscription['id'] == subscription_id:
            subscription['phone_number'] = data['phone_number']
            subscription['plan'] = data['plan']
            subscription['status'] = data['status']
            return jsonify(subscription)
    return 'Subscription not found', 404

if __name__ == '__main__':
    app.run()
