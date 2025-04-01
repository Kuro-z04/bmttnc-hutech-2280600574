from flask import Flask, request, jsonify
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = data.get('key')
    if not plain_text or not key:
        return jsonify({'error': 'plain_text and key are required'}), 400
    try:
        key = int(key)  # Chuyển key thành số nguyên
        if key < 1:
            return jsonify({'error': 'key must be at least 1'}), 400
    except ValueError:
        return jsonify({'error': 'key must be a valid integer'}), 400
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if not cipher_text or not key:
        return jsonify({'error': 'cipher_text and key are required'}), 400
    try:
        key = int(key)  # Chuyển key thành số nguyên
        if key < 1:
            return jsonify({'error': 'key must be at least 1'}), 400
    except ValueError:
        return jsonify({'error': 'key must be a valid integer'}), 400
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)