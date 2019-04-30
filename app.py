from flask import Flask
from flask_cors import CORS
from flask import request
from flask import jsonify

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def index():
    if request.args.get('user') is None:
        return 'Hello to Flask MicroService :)'
    else:
        return request.args.get('user')


if __name__ == '__main__':
    # manager.run()
    port = int(os.environ.get("PORT", 9997))
    app.run(debug=False, host='0.0.0.0', port=port)
