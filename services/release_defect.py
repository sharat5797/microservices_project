from services.measures import Measures

class ReleaseDefects(Measures):
    
    def getMeasureResponse(self):
        return "getMeasureResponse invoked from ReleaseDefects"
    
    def getSource(self):
        return "get source invoked from ReleaseDefects"