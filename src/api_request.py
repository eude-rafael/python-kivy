import requests
import json

class remoteGet:
    def get(userUrl):
        # URL da API que você deseja acessar
        url = "https://eude.com.br/api.php"

        # Dados a serem enviados no corpo da requisição POST
        data = {
            'url': userUrl
        }

        # Converte os dados em JSON
        json_data = json.dumps(data)

        # Define o cabeçalho da requisição com o tipo de conteúdo JSON
        headers = {'Content-Type': 'application/json'}

        # Desabilita a verificação do certificado SSL (USE COM CAUTELA!)
        response = requests.post(url, data=json_data, headers=headers, verify=False)

        # Verifica se a solicitação foi bem-sucedida
        if response.status_code == 200:
            # Converte a resposta JSON em uma lista Python
            response_data = response.json()

            # Verifica se a lista não está vazia (caso o JSON retorne mais de um objeto)
            if response_data:
                # Acessa o primeiro elemento da lista (que é um dicionário)
                primeiro_objeto = response_data

                # Verifica se a chave 'recebido' está presente no dicionário
                if 'recebido' in primeiro_objeto:
                    return primeiro_objeto['recebido']
                     
                else:
                   return  "Chave 'recebido' não encontrada no JSON."
            else:
                return  "JSON vazio."
        else:
             return  "Erro na solicitação:", response.status_code


