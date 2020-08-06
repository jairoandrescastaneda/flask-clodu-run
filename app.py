import os
from dotenv import load_dotenv

from flask import Flask

load_dotenv()
app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'Jairo')
    return 'Hello {}!\n'.format(target)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))