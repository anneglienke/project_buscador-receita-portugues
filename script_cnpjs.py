# -*- coding: utf-8 -*-
import json
import requests
import time
import pandas as pd

listaCnpj = pd.read_excel("Nome_arquivo_com_CNPJs.xlsx")

ListaCompleta = []
i=1
for cnpj in listaCnpj["CNPJ"]:

    try:

        url = 'https://www.receitaws.com.br/v1/cnpj/%s' % cnpj
        req = requests.get(url)
        dicionario = json.loads(req.text)

        print("CNPJ nº"+str(i))

        dados = {}

        if 'cnpj' in dicionario:
            dados["cnpj"] = dicionario["cnpj"]
        if 'abertura' in dicionario:
            dados['abertura'] = dicionario['abertura']
        #if 'atividade_principal' in dicionario:
        #    dados['atividade_principal'] = dicionario['atividade_principal']
        if 'nome' in dicionario:
            dados["razÃ£o"] = dicionario["nome"]
        if 'fantasia' in dicionario:
            dados['fantasia'] = dicionario['fantasia']
        if 'email' in dicionario:
            dados['email'] = dicionario['email']
        if 'telefone' in dicionario:
            dados['telefone'] = dicionario['telefone']
        if 'logradouro' in dicionario:
            dados['logradouro'] = dicionario['logradouro']
        if 'numero' in dicionario:
            dados['numero'] = dicionario['numero']
        if 'bairro' in dicionario:
            dados['bairro'] = dicionario['bairro']    
        if 'cep' in dicionario:
            dados['cep'] = dicionario['cep']               
        if 'municipio' in dicionario:
            dados['municipio'] = dicionario['municipio']
        if 'uf' in dicionario:
            dados['uf'] = dicionario['uf']
        #if 'qsa' in dicionario:
        #    dados['qsa'] = dicionario['qsa']  
        if 'capital_social' in dicionario:
            dados['capital_social'] = dicionario['capital_social']
        if 'situacao' in dicionario:
            dados ['situacao'] = dicionario['situacao']
        if 'tipo' in dicionario:
            dados['tipo'] = dicionario['tipo']

        ListaCompleta.append(dados)
        
        i=i+1

        print("Aguarde...")
       
        time.sleep(21)

    except Exception as e:
        print(e)
        print(req.text)
        time.sleep(21)

df= pd.DataFrame(ListaCompleta)

df.to_excel("Nome_do_novo_arquivo_enriquecido.xlsx")

print("Salvo no excel. Arquivo: Nome_do_novo_arquivo_enriquecido.xlsx.")

