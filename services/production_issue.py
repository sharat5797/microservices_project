from services.measures import Measures


class ProductionIssue(Measures):
    def getMeasureResponse(self):
        return "hello i am production issue"

    def getSource(self):
        return "temp"
