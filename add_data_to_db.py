import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("agenda-ece58-firebase-adminsdk-39kgg-96d30e3987.json")
firebase_admin.initialize_app(cred)


# Acessando a base de dados
db = firestore.client()


# Passar informações de clientes para base de dados
doc_ref = db.collection('users').document('J3GKQOqo7FNSevlcpifu').collection('clients').document('teste')
doc_ref.set({
    'nome_fantasia': 'Teste teste teste',
    'qualquer coisa': 'qualquer coisa escrita'

})