from flask import Flask, jsonify
from injector import inject
from flask_injector import FlaskInjector
from services.buildtime import BuildTime
from services.production_issue import ProductionIssue
from services.release_defect import ReleaseDefects
from services.measures import Measures

app = Flask(__name__)

class MeasureBinder:
    @inject
    def __init__(self, request):
        self.request = request

    def configure(self, binder):
        measure = self.request.args.get('measures')
        if measure == 'buildtime':
            binder.bind(Measures, to=BuildTime, scope=singleton)
        elif measure == 'releasedefect':
            binder.bind(Measures, to=ReleaseDefects, scope=singleton)
        elif measure == 'productionissues':
            binder.bind(Measures, to=ProductionIssue, scope=singleton)

FlaskInjector(app=app, modules=[MeasureBinder(request=request)])  # Pass the request here

@app.route("/measures/<string:param>", methods=["GET"])
@inject
def measures_result(param, measures: Measures):
    return jsonify(measures.getMeasureResponse())

if __name__ == '__main__':
    app.run(debug=True, port=8001)
