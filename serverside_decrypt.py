# -> 18/09/2024 15.35 
# -> author: Mustafa Osman Dilmaç (@qdilmac)
# -> Data ecnryption-decryption tests for future use, using basic encryption methods and generic libraries.
# -> Server-side (receiver, e.g. Main computer)

from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# -> Enkripte edilen veriyi alacak yol
@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json

    if not data:
        return jsonify({"message": "No data received"}), 400

    # -> Gelen veri ve anahtarı al
    encrypted_data = data.get('data')
    key = data.get('key')

    if not encrypted_data or not key:
        return jsonify({"message": "Missing encrypted data or key"}), 400

    # -> Deşifre işlemleri
    try:
        cipher_suite = Fernet(key.encode())
        decrypted_data = cipher_suite.decrypt(encrypted_data.encode()).decode()
        print(f"Şifreli veri: {encrypted_data}")
        print(f"Anahtar: {key}")
        print(f"Deşifre veri: {decrypted_data}")
        return jsonify({"message": "Veri başarıyla alındı ve deşifre edildi.", "decrypted_data": decrypted_data}), 200
    except Exception as e:
        return jsonify({"message": f"Deşifreleme işlemi başarısız!: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)