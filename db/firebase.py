import os

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, storage

# Load environment variables from the .env file
load_dotenv()

# Set up Firebase Admin SDK credentials using environment variables
firebase_config = {
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDc6cJ02Exqgcen\n3L3Ebh9IfrEORLFiSDfAl4wEr5lm5EjTFeTksTipJOoYqZIsAT8rkYDxVoCO/chi\nFmy4EFpTNR9Pxs+1mMwIDNPhSnP3hTNcG5xnNcGieRFafVWxyea2PHQ5A6L498Le\np+/sPlZGZYF1IYj7WG3gAtYEBoaYq24i2foVfOYR0rOdgn86ay9lsdlWBNlBcrWE\nT6fG0miSVgrA2hi1WpJKltFR8o4uvVhlh38tmQBUaDLHJKdiG7lAfFGh8+NlodJk\nLG0cr33lg48q5WRmUtNbuoDZRraiEy8xHGOufTvGtehWxEKnA3Jkl82uljecMqzY\ncn/i+PZdAgMBAAECggEAPLhd1Br9ygqY87k3Sc4Q+C6mgOr9rKt3845UFJelfQQD\nRk3Ox9M0ZT15wMSfIkxHbjTEsdEabfMwiFFsmZ0ZDqTb0eQuBFaWwiGwfUynGmI4\nzzjhoPbEHeHUFMC9dKwvp2hvc5pdybvkCqozRoaN1TSiRC0vBxLzxG5TH/EhPsXh\nGLcZmCZYfnVe8aIEP7yIp714W2YJHOUZHcYVOmwHDzBFT/C1b6nLq4hoeWxlW8/E\nL8XM2LY0AQ+YzvOCQ3CY0Zo9XvzsoK6iYfgYGKtKJ1AUVK89oachN3lMS4VQRaHr\nyybUzKB/xSlUUVLMEGNANX0zEhcH98aTvpNi9M0SqwKBgQD4hi658wQZ3zD85Ktk\nCjte4gNOPftgy8lHBowZku+kffM0zUeESGv4Bi3ehedL+N7CIV8/6mBBWSm7uZU7\ny/csMHLXVdcZ9X+lYFOpdpQJ7JquwRCSQbeXGxeoGOpzLVASj2LRhVlYmm+nf8wQ\n5JdqHJjN7SNzSLrq86pG2SuPowKBgQDjjvO1/NOHgkvpr0Ty9XQWoV40OHDd2l58\nnL4FIc/qIMYcUSfJ627X0BZSgdjlXQNx12kXwRfANPvxTNb+ZlgbXgd9DRZKYMYw\nyWbqG9SReVuKYxZA5v7cOweJ9T12f2k15hvxry+/l45c8OAklSzNwS3svlsYwnsV\nJmNQKjnB/wKBgFAkhUD1uybUsKl83EBAhHDOlZ5PopbOYLQEyn0cwybabuliIWPp\nLtgmtfgCWlpHgR49QMgNvsiUBj9BU3ybA7Q+U2pZhioa3vTnoVMOqCKjKCaen8dq\nZdfWpsRQdJp7zEyP7KAATpWiB8uODLKN5L4VRrlxdXMhyxUlSo3aTo/dAoGAYw1D\nmlDuBos53gNz4Mnk+UDOj66NupQmEtnrgLJiHUic05Cj4CnB+uDSBqIMtnIRYMli\nLnvXicvGaxeGcgA8k9UPL2i17jRHsM7KJFdu5M/Nf+R3uFKUV2q+cle0pFL7igGa\n4k3eW+htiJk1B9eDRCC1i9qkLpfhGai3DBsFPyMCgYEA0+akoREfBzFXOn8ARxjE\nsofvnUxp9tjeFAWqf2TK6IfFVj/VapTfyS9j27z7mRwNtzp5QmNcPKxYQlPCzITO\nNGwHJqQjTapoz6RcuRviOB81KTMwDciesksoFnajlPU/OAjRY0ZV0qTcVEMTd/6F\nrcTGpF/pZM2EDiRtLAw4bAE=\n-----END PRIVATE KEY-----\n",
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
}

# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {
    'storageBucket': f"{os.getenv('FIREBASE_PROJECT_ID')}.appspot.com"
})

# Firebase Storage bucket reference
bucket = storage.bucket()
__all__ = ['bucket']
