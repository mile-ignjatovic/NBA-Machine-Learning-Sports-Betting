import firebase_admin
from firebase_admin import credentials, db

def init():
    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": "bet-ml-f1c3b",
        "private_key_id": "58ddad1bbf2371516aaf0683c0626147c1a4bcb4",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC9m1hlbQM5tpLC\n1Z677gGr9UY9qacTOVmuX+vEd+fCzqHcLguyn5cMirzf8g9q1D4tOZKIVNqTLD7y\nQKOFw2y2tx6ZWAtO+H+e7kykTMXXVyrjKabDoJ//NhJvLTYW3Ubs7gM+zRIZKi/l\nsCg7l7/Fq51uHCbm0Gz9xkWxB8iVj4qwXT2NU+ygCiXSvqc7KHu12Z/KLH0zreFK\nel8ib8TZjlJdgGiEFjPHb1X3jLpwLs6n6GHosxYWfTZHVywuyOnsvmpabDbnDelw\ns3ETIDDRbGLGQXrEbat+ut9ay3AJTjYoDh+8cGVPqXM8sIQJgvPJ+cC5/oFIruV/\nv2hkmvGRAgMBAAECggEAGFKQMVqdmk6wXuv2U9dBQaTSIODdfNrThUnqvaZABb5q\nBwulFoHgZ4x4lCXCEosterGy+WghLdX0MTFXiLY8AOhWtYcU1EmOXX3mOQFcM7aL\n2t4h9WBqhduS284p7R7vlT8nDWxTEQVXZZiGYLajtCDCrjhQSTWddaR0ljQQaBbs\nNw3CETgF5wxNOS53l7/ESx/W7Fsb5HpU6aHI0soKeZypFNXybx21o3bnhRcU7/GZ\nDT/XBIUXDjgKjizbVvQqaFzSbshM5QBDYEniKnYn+u8eLfwCRBSYH52dTHYpYNWp\nGRacKUsmGx7/7z+3j3H3wfvr15ZBi2N8Pmpfh61XfQKBgQDmqLO9TBuIEls1Qldc\nzLyVYfJLHWzPFK6BRb/PYuERRy8md39mR8FoYHdhksLuODI5idNirg7WAUZwCPrJ\ntL09eXMxGy+wHWbO3fiBCCrtBXE7nR0pbvAMWrJHCF7D/8RXufcvA+5F1sE+78YJ\nnPQ87EyR50XIPmbjTdJvMeR59wKBgQDScAxfANBmSXeh/HubunoHENECRNl+sPjQ\n9i63rqlOsuOchVopFsfvwVR+wyrfxHChdGnTJ+FwXlLLx3AZ40Sqoz8zp/cEY10Y\nykuI5Tg+QINqulsm6cpZ+wY48py6cMvMA9M9lN8TvZIG3DpjEDbrHvkKim2oVV9A\n9QkkYDXOtwKBgCVSLqL2aY3+yls3vML7LZhOHNIilLR8+C9ahcqciSYuimaC904p\nVhX5ZdeX04qP9TByKI3S8/uUgT0ndsykPepweD790x1/5F6cc9UM6UUomEW5Cjrm\nBFk7Y5UyuYKlI7O+F0y4KhmKwgHY8gYkKzCgW1NQRG4+Co/Ey8PKItnJAoGBALGh\nk0++SCuPaER783sIdWjxcPwRUeX3TJBWviiebpvXtPmyNuDoMezXrJMz+0TXdJtU\nwN9Ukp9ff1Q0DRRNGvFOy1K3PXOezD7Yw9nSYx9pJYU5uSenwP8jPaVkZZebDuwv\nbmhU+diX9GOGEmL8lN7zThTvtJCbP8R9EjJ6Y/ERAoGBALtrw4keJfU7Sb2kPvV5\nzgxc7CRkxrq9sx8QhEknp7PO5JcIfVYXl1x5gmCEwPRjZ75o2qDO6ufzo3b8yEnZ\nq1xoy4//ryJLnKMCqE07tyzuOaq6QCeM/Il0xIjD+89gS6uGpREqe92hZ6IBBvtl\nP3U6TpD19o5EXLsafqOIYVpQ\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-e6exd@bet-ml-f1c3b.iam.gserviceaccount.com",
        "client_id": "102720562154089803038",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-e6exd%40bet-ml-f1c3b.iam.gserviceaccount.com"
        })
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://bet-ml-f1c3b-default-rtdb.europe-west1.firebasedatabase.app/'
    })

def push_predicition(data):
    ref = db.reference('/all-predictions')
    new_child_ref = ref.push()
    result = new_child_ref.set(data)
    handle_response(result)
        
def handle_response(result):
    if result is None:
        return True # Success
    else:
        raise ValueError('FALIURE')
       

def test_db_connection():
    data = {'foo': 'bar'}
    # Get a reference to the Firebase Realtime Database
    ref = db.reference('/test')
    new_child_ref = ref.push()
    result = new_child_ref.set(data)
    handle_response(result)

   
