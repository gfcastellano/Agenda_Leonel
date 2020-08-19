""" import firebase_admin
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

print(len(dados_visitas)) """





import requests
import json


url_db = 'https://agenda-leonel.firebaseio.com/users/'
user_id = 'I10r2hxrlpU6Qmsf9DELnMcH9D22/'


with open('clientes.json', 'r') as file:
    dados_clientes = json.load(file)
    print('clientes.json carregado com sucesso,' 'tamanho:',len(dados_clientes))
""" 
for cliente in dados_clientes:
    dados ={
        
        'codigo'                   = novo_cliente['codigo']         
        'nome_fantasia'            = novo_cliente['nome_fantasia'] 
        'bairro'                    = novo_cliente['bairro']  
        'endereco'                 = novo_cliente['endereco']
        'bairro'                  = novo_cliente['bairro'] 
        'numero'                     =  novo_cliente['numero'] 
        'bairro'                     = novo_cliente['bairro']
        'cidade' = novo_cliente['cidade']         = cidade
        'telefone_fixo' =  novo_cliente['telefone_fixo']  = 
        'perfil_cliente' = novo_cliente['perfil_cliente'] = perfil_cliente
        'nome_1' = novo_cliente['nome_1']         = nome_1
        'telefone_1' = novo_cliente['telefone_1']     = telefone_1
        novo_cliente['tipo_1']         = tipo_1
        novo_cliente['nome_2']         = nome_2
        novo_cliente['telefone_2']     = telefone_2
        novo_cliente['tipo_2']         = tipo_2
        novo_cliente['nome_3']         = nome_3
        novo_cliente['telefone_3']     = telefone_3
        novo_cliente['tipo_3']         = tipo_3
        novo_cliente['data']           = str(date.today())
        novo_cliente['razao_social']   = razao_social
        novo_cliente['razao_social']   = razao_social
        novo_cliente['cnpj']           = cnpj
        novo_cliente['cep']            = cep

        novo_cliente['lat']            = lat
        novo_cliente['lon']            = lon

        novo_cliente['banho']          = banho
        novo_cliente['tosa']           = tosa
        novo_cliente['pet_shop']       = pet_shop
        novo_cliente['clinica']        = clinica

        novo_cliente['cliente']        = ''
        novo_cliente['therapet']       = ''
        novo_cliente['tesoura']        = ''
        novo_cliente['tap_higienico']  = ''

    }
 """
dicionario = {
        'codigo':  '',
        'nome_fantasia' :'',
        'endereco'      :'',
        'bairro'        :'',
        'telefone'      :'',
        'contato'       :'',
        'perfil'        :'',
        'banho'         :'',
        'tosa'          :'',
        'clinica'       :'',
        'razao_social'  :'',
        'cnpj'          :'',
        'cep'           :'',
        'therapet'      :'',
        'tesoura'       :'',
        'tap_higienico' :'',
}

for key in dicionario.keys():
    print(key)
""" 
to_database = json.dumps(dados)
print('to_database:',to_database) """

""" if 'visita' not in list(dados.keys()):
    print('Iniciou o patch')
    response = requests.patch(url = self.url_db + self.user_id + 'clientes/' + str(codigo - 1) + '.json', 
                            data = to_database)
    print('Fez o patch dos clientes?', response.ok)
    #print('Conteudo', response.content.decode()) """