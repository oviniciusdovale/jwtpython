from flask import Flask, jsonify
import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

private_key = os.getenv('PRIVATE_KEY')

if not private_key:
    raise ValueError("Chave privada não encontrada no arquivo .env")

@app.route('/generate-token', methods=['GET'])
def generate_token():
    payload = {
        'iss': 'fluxoidv2@08db60a1-ac4e-43c9-b3f2-9ae0f5939254.iam.acesso.io',
        'scope': '*',
        'aud': 'https://identityhomolog.acesso.io',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        'iat': datetime.datetime.utcnow()
    }

    try:
        token = jwt.encode(payload, private_key, algorithm='RS256')
        return jsonify(token=token)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(port=3000)
