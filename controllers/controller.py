from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def ping_server():
    return "Welcome to Microservices world"

@app.route('/user')
def get_user():
    return jsonify({"name":"sharat","email":"sharathegde772@gmail.com","location":"banglore"})


@app.route('/admin')
def get_admin():
    return jsonify({"name":"raju","email":"raju2@gmail.com","location":"banglore"})
   

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5001)
