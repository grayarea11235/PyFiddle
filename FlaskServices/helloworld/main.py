from flask import Flask, request, jsonify

# Service goes here
app = Flask(__name__)
  
  
@app.route('/hello', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data": "Hello World!"}
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug = True)
