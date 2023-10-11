from services.measures import Measures


class ProductionIssue(Measures):
   
    def getMeasureResponse(self):
        return "this is production issue"

    def getSource(self):
        pass
