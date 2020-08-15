iimport firebase_admin
from firebase_admin import credentials, firestore
import json

cred = credentials.Certificate("agenda-ece58-firebase-adminsdk-39kgg-96d30e3987.json")
firebase_admin.initialize_app(cred)


# Acessando a base de dados
db = firestore.client()


# Passar informações de clientes para base de dados
o# Ler dados de clientes
with open('clientes.json', 'r') as file:
    dados_clientes = json.load(file)
# Colocar cada cliente como um documento dentro da data base
doc_ref = db.collection('users').document('J3GKQOqo7FNSevlcpifu').collection('clientes')

for cliente in dados_clientes:
    doc_ref.add(
        {
            "codigo": cliente['codigo'],
            "nome_fantasia": cliente['nome_fantasia'],
            "endereco": cliente['endereco'],
            "numero": cliente['numero'],
            "cidade": cliente['cidade'],
            "bairro": cliente['bairro'],
            "lat": cliente['lat'],
            "lon": cliente['lon'],
            "telefone_fixo": cliente['telefone_fixo'],
            "perfil_cliente": cliente['perfil_cliente'],
            "nome_1": cliente['nome_1'],
            "telefone_1": cliente['telefone_1'],
            "tipo_1": cliente['tipo_1'],
            "nome_2": cliente['nome_2'],
            "telefone_2": cliente['telefone_2'],
            "tipo_2": cliente['tipo_2'],
            "nome_3": cliente['nome_3'],
            "telefone_3": cliente['telefone_3'],
            "tipo_3": cliente['tipo_3'],
            "data": cliente['data'],
            "banho": cliente['banho'],
            "tosa": cliente['tosa'],
            "pet_shop": cliente['pet_shop'],
            "clinica": cliente['clinica'],
            "cliente": cliente['cliente'],
            "razao_social": cliente['razao_social'],
            "cnpj": cliente['cnpj'],
            "cep": cliente['cep'],
            "therapet": cliente['therapet'],
            "tesoura": cliente['tesoura'],
            "tap_higienico": cliente['tap_higienico']
        }
    )
# Ler dados de visitas
with open('visitas.json', 'r') as file:
    dados_visitas = json.load(file)
# Colocar cada cliente como um documento dentro da data base
doc_ref = db.collection('users').document('J3GKQOqo7FNSevlcpifu').collection('visitas')

for visita in dados_visitas:
    doc_ref.add(
        {
            "data": visita['data'],
            "nome_fantasia": visita['nome_fantasia'],
            "contato": visita['contato'],
            "informacoes": visita['informacoes'],
            "codigo": visita['codigo'],
            "visita": visita['visita']
        }
    )

print(len(dados_visitas))