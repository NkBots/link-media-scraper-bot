import requests ,json, time
from decouple import config



login_id = config('API_USERNAME', "wusu7373eud")
key_id = config('API_PASSWORD', "xyz11334")

def get_ticket(file_id):
    headers = {'file':file_id,'login':login_key,'key':key}
    response = requests.get("https://api.strtape.tech/file/dlticket?",headers)
    data = json.loads(response.text)

    result = data.get('result')
    #ticket = data.get('result').get('ticket')
    return result
