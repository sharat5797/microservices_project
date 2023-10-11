from flask import Flask, jsonify, request
from configure import configure
from injector import inject
from flask_injector import FlaskInjector
from services.buildtime import BuildTime
from services.production_issue import ProductionIssue
from services.release_defect import ReleaseDefects
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

@app.route("/measures/<string:param>", methods=["GET"])
@inject
def measures_result(param,buildtime:BuildTime,productionIssue:ProductionIssue,releaseDefect:ReleaseDefects):
    if "buildtime" in param:
        return buildtime.getMeasureResponse()
    elif "productionissue" in param:
        return productionIssue.getMeasureResponse()
    elif "relreleasedefect" in param:
        return releaseDefect.getMeasureResponse()

@app.route("/measures", methods=["GET"])
@inject
def all_measures_result(buildtime:BuildTime,productionIssue:ProductionIssue,releaseDefect:ReleaseDefects):
    return jsonify({
        "buildtime": buildtime.getMeasureResponse(),
        "productionissue": productionIssue.getMeasureResponse(),
        "relreleasedefect": releaseDefect.getMeasureResponse()
    })

# @inject
# def get_build_time(buildtime:BuildTime):
#     return jsonify(buildtime.getMeasureResponse())

# @inject
# def get_producation_issue(productionIssue:ProductionIssue):
#     return jsonify(productionIssue.getMeasureResponse())

# @inject
# def get_release_defect(releaseDefect:ReleaseDefects):
#     return jsonify(releaseDefect.getMeasureResponse())

FlaskInjector(app=app, modules=[configure])


if __name__ == '__main__':
    app.run(debug=True, port=8001)