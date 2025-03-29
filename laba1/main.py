from flask import Flask, request, jsonify

app = Flask(__name__)

class Contact:
    def __init__(self, id=0, username="", given_name="", family_name="", full_name="", phone=[], email=[], birthdate=""):
        self.id = id
        self.username = username
        self.given_name = given_name
        self.family_name = family_name
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.birthdate = birthdate

class Group:
    def __init__(self, id=0, title="", description="", contacts=[]):
        self.id = id
        self.title = title
        self.description = description
        self.contacts = contacts

@app.route('/api/v1/contact', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_contact():
    return jsonify(Contact().__dict__), 200

@app.route('/api/v1/group', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_group():
    return jsonify(Group().__dict__), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6080)