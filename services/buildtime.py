from services.measures import Measures

class BuildTime(Measures):

    def getMeasureResponse(self):
        return "this is the measure"
    
    def getSource(self):
        return "source is jira"
    