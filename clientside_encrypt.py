# -> 18/09/2024 15.35 
# -> author: Mustafa Osman Dilmaç (@qdilmac)
# -> Data ecnryption-decryption tests for future use, using basic encryption methods and generic libraries.
# -> Client-side (sender, e.g. Raspberry Pi)

import requests
from cryptography.fernet import Fernet
import json

# -> Enkripsiyon için anahtar oluştur. Bu anahtar ile veri şifrelenir ve anahtar ile şifre çözülür.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# -> Veriyi şifreleme fonksiyonu
def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Örnek veri -> Bunun yerine sensör verisi vs eklenir.
data = """Gerilir zorlu bir yay, Oku fırlatmak için;
            Gece gökte doğar ay, Yükselip batmak için.
            Mecnûn inler, kanını Leylâ’ya katmak için.
            Cilve yapar sevgili, Gönül kanatmak için.
            Şair neden gam çeker? Şiir yaratmak için.
            Dağda niçin bağrılır? Feleğe çatmak için.
            Açılır tatlı güller, Arılar tatmak için.
            Göğse çiçek takılır, Solunca atmak için.
            Tanrı kızlar yaratmış, Erlere satmak için.
            İnsan büyür beşikte, Mezarda yatmak için.
            Kahramanlar can verir, Yurdu yaşatmak için…"""

# -> Veriyi şifrele
encrypted_data = encrypt_data(data)

# -> Enkripte veri ve anahtardan oluşan bir json oluştur
# -> PAYLOAD İÇERİSİNDE ANAHTARI DA GÖNDERMEK CİDDİ BİR RİSK!!! BURADA SADECE TEST AMAÇLI GÖNDERİLİYOR.
payload = {"data": encrypted_data.decode(), "key": key.decode()} # -> decode() metodu byte veriyi stringe çevirir. dictionary olarak gönderiyoruz key:value şeklinde.

# -> Flask sunucusunun adresi
server_url = "http://192.168.1.110:5000/receive_data"

try:
    # Send the encrypted data to the server
    response = requests.post(server_url, json=payload)
    print(f"Payload: {payload}")
    print(f"Şifrelenmiş Data: {encrypted_data}")
    print(f"Şifrelenmiş anahtar: {key}")
    print(f"Server cevap kodu: {response.status_code}")
    print(f"Server cevabı: {response.text}")
except requests.exceptions.ConnectionError as e:
    print(f"Bağlantı hatası: {e}")