import json
from flask import Response 

def json_response(data=None, message='', status=400):
    return_data = {
        'message': message
    }

    if(data):
        return_data['data'] = data
        del return_data['message']
    
    if(not data and data != None):
        return_data['data'] = None
        return_data['message'] = 'Nenhum resultado encontrado'

    return Response(json.dumps(return_data), status=status, mimetype='application/json')
    