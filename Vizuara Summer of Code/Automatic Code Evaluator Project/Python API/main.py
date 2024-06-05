# flask is the server that is running the API
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Vizuara"

# GET - Request data from a specified resoure 
# POST - create a resource 
# PUT - update a resource
# DELETE - delete a resource

# GET route
@app.route("/get-user/<user_id>")
def get_user(user_id):

    # Mock user data
    user_data = {
        "user_id": user_id,
        "name": "Ubayed Bin Sufian",
        "email": "ubayedbinsufian@gmail.com"
    }

    # Check for additional query parameter "extra"
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200  # 200 is the default success code 

if __name__=="__main__":
    app.run(debug=True)  # This starts the Flask development server