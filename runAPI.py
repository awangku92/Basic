from flask import Flask, request
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class HW(Resource):
#     def get(self):
#         return {'hello' : 'world'}

# api.add_resource(HW, '/')

# class test(Resource):
#     def get(self):
#         return {'a' : 'b'}

# api.add_resource(test, '/test')

# class testVar(Resource):
#     def get(self, que):
#         return {'var' : que}

# api.add_resource(testVar, '/testVar/<que>')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# API : localhost:5001/t
@app.route("/t", methods=['GET', 'POST'])
def test():
    return "test!"

# API : localhost:5001/user/abc
@app.route("/user/<query>", methods=['GET', 'POST'])
def users(query):
    return "Hello {}!".format(query)

# API : localhost:5001/filter/abc?age=10
@app.route("/filter/<query>", methods=['GET', 'POST'])
def filter(query):
    age = request.args.get('age')
    return "{}'s age is {} year(s) old".format(query, age)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)