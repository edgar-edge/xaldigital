from flask import Blueprint, jsonify

#Models
from models.accountModel import AccountModel

main=Blueprint('account_blueprint', __name__)

@main.route('/')
def get_client():
    try:
        clients = AccountModel.get_account()
        return jsonify(clients)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500