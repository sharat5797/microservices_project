from flask import jsonify

class User:
    def __init__(self):
        self.data = [{"id":1,"name":"user1", "email":"user1@gmail.com"}, {"id":2,"name":"user2", "email":"user2@gmail.com"}]

    def createUser(self, user1):
        self.data.append(user1)
        return jsonify({"message":'added user successfully', 'data':self.data[-1]})
    
    def getUserList(self):
        return jsonify(self.data)
    
    def deleteUser(self, resourceId):
        del self.data[int(resourceId)-1]
        return jsonify({'message':'User deleted'})