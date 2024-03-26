from flask import Blueprint, request, Response
from .handlers import ContactHandler
contactBlueprint = Blueprint('contact', __name__, url_prefix='/contacts')

@contactBlueprint.route('/', methods=['GET', 'POST'])
@contactBlueprint.route('/<uuid:id>', methods=['GET', 'PATCH', 'DELETE'])
def get_contacts(id=None):
    
    match request.method:
        case 'GET':
            return ContactHandler().get(id)
        case 'POST':
            data = request.json
            return ContactHandler().post(data)
        case 'PATCH':
            data = request.json
            return ContactHandler().patch(id, data)
        case 'DELETE':
            return ContactHandler().delete(id)
        case _:
            return '', 405

