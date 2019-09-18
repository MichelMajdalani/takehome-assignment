from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/shows", methods=['GET'])
def get_all_shows():
    return create_response({"shows": db.get('shows')})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


# TODO: Implement the rest of the API here!

@app.route('/shows/<id>', methods=['GET'])
def show_show(id):
    queriedData = db.getById('shows', int(id))
    if queriedData is None:
        return create_response(status=404, message="No show with this id exists")
    return create_response(queriedData)

@app.route('/shows', methods=['POST'])
def create_show():
    message = ''
    # Find how to access the body of a request
    # Check if there is an error in parameters entered
    name = request.form['name']
    if len(name) == 0:
        message += 'You did not enter a name. '

    episodes_seen = request.form['episodes_seen']
    print(episodes_seen)
    if len(episodes_seen) == 0:
        message += 'You did not enter an episodes_seen number. '

    if len(message) > 0:
        return create_response(status=422, message=message)
    
    # Convert to correct format before adding to database
    episodes_seen = int(episodes_seen)
    # Create object in database
    new_data = db.create('shows', {"name": name, "episodes_seen": episodes_seen })
    # Create response
    return create_response(status=201, data=new_data)

@app.route('/shows/<id>', methods=['PUT'])
def update_show(id):
    # Get data from database
    queriedData = db.getById('shows', int(id))
    if queriedData is None:
        return create_response(status=404, message='The object with this specified id does not exist.')
    
    # Extract information from request
    name = request.form['name']
    episodes_seen = request.form['episodes_seen']
    
    # Verify whether they are empty or not. If not, update
    if len(name) > 0:
        queriedData['name'] = name

    if len(episodes_seen) > 0:
        queriedData['episodes_seen'] = int(episodes_seen)

    return create_response(status=201, data=queriedData)


"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
