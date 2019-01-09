from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api

from transform import Transform

app = Flask(__name__)
api = Api(app)


class GetData(Resource):
    def get(self):
        return jsonify({'data': 'send your data like this'})

    def put(self):
        data = request.get_json(force=True)
        get_results = Transform().transform(data)
        return jsonify(output=get_results)

    def post(self):
        data = request.get_json(force=True)
        get_results = Transform().transform(data)
        return jsonify(output=get_results)


@app.route('/')
def swagger():
    return render_template('index.html')


api.add_resource(GetData, '/api')

if __name__ == '__main__':
    app.run(debug=False)
