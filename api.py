from flask import Flask,request,jsonify
from flask_jwt_extended import JWTManager, create_access_token
import new

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

app.register_blueprint(new.opp)
if __name__ == "__main__":
    app.run()
