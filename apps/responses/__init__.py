def customResponse(data, status_code:int, message='No message', error=False):
    response = {
        'data': data if not error else 'No data',
        'error': error,
        'message': message
    }
    print(response)
    return response, status_code