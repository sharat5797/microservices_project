from flask import Flask, request
from configure import configure
from injector import inject
from flask_injector import FlaskInjector
from services.service import User


app = Flask(__name__)


@app.route("/postUser", methods=["POST"])
@inject
def postUser(user:User):
    user1 = request.json
    return user.createUser(user1)
    

@app.route("/getUser", methods=["GET"])
@inject
def getUser(user:User):
    return user.getUserList()

@app.route("/deleteUser/<resourceId>", methods=["DELETE"])
@inject
def deleteUser(resourceId, user:User):
    return user.deleteUser(resourceId)

FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run(debug=True, port=8001)