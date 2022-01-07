from source.tasks import sum_of_numbers
from flask import (
   Flask,
   request,
   jsonify,
)


app = Flask(__name__)


@app.route("/", methods = ['GET'])
def home():
   return jsonify({'response': "Hello World!"}), 200


@app.route("/sum-numbers", methods = ['POST', 'GET'])
def sum_numbers_with_celery():
   number1 = request.args.get("number1")
   number2 = request.args.get("number2")
   result = sum_of_numbers.apply_async(args=[number1, number2])
   return jsonify({'response': "sucessfull", "task_id": result.id}), 200