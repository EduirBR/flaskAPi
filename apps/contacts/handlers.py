from .models import Contact
from apps.responses import customResponse

class ContactHandler:

    def get_by_id(self,id):
        contact = Contact.query.get(id)
        if not contact:
            return customResponse(None, 404, 'Contact not found', True)
        return customResponse(contact.toJson(), 200, 'Contact retrieved successfully')

    def get(self, id = None):
        if id:
            return self.get_by_id(id)
        contacts = Contact.query.all()
        contacts_list = []
        for contact in contacts:
            contacts_list.append(contact.toJson())
        return customResponse(contacts_list, 200, 'Contacts retrieved successfully')
    
    def post(self, data):
            try:
                contact = Contact(**data)
                contact.save()
                return customResponse(contact.toJson(), 201, 'Contact created successfully')
            except ValueError as error:
                return customResponse(None, 400, str(error), True)

    def patch(self, id, data):
        contact = Contact.query.get(id)
        if not contact:
            return customResponse(None, 404, 'Contact not found', True)
        try:
            for key, value in data.items():
                if contact.__getattribute__(key) == value:
                    continue
                setattr(contact, key, value)
            contact.save()
            return customResponse(contact.toJson(), 200, 'Contact updated successfully')
        except ValueError as error:
            return customResponse(None, 400, str(error), True)
    
    def delete(self, id):
        contact = Contact.query.get(id)
        if not contact:
            return customResponse(None, 404, 'Contact not found', True)
        contact.delete()
        return customResponse(None, 204, 'Contact deleted successfully')
