from flask import Flask, request, jsonify
import os 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def select_all():
    return 'Hello World Flask42!!'

if __name__ == "__main__":
    app.run(debug=True)