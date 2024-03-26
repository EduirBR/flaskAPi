from flask import Blueprint, request, jsonify
from .models import Contact

contactBlueprint = Blueprint('contact', __name__, url_prefix='/contacts')

@contactBlueprint.route('/', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([contact.toJson() for contact in contacts])

