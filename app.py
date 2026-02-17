# import the flask framework
from flask import *


# below we create a webserver based application
app = Flask(__name__)



# below we create the home route
# Routing:This is mapping/connecting different resources to different functions.We do this by the help of a decorator.
@app.route("/api/home")
def home():
    return jsonify({"message" : "Home route accessed"})





# below is the products route
@app.route("/api/products")
def products():
    return jsonify({"message" : "Welcome to the products route"})





# below is a route for addition
@app.route("/api/calc" , methods=["POST"])
def calculator():
    if request.method == "POST":
        number1 = request.form["number1"]
        number2 = request.form["number2"]

        sum = int(number1) + int(number2) 

        return jsonify({"The answer is " : sum})

# create a route that is able to calculate the simple interest given the principal as 20000,rate as 7% and time as 8 years

@app.route("/api/simp" , methods=["POST"])
def simpleinterest():
    if request.method == "POST":
        principle = request.form["principle"]
        rate = request.form["rate"]
        time = request.form["time"]
        product = (int(principle) * int(rate) * int(time))/100

        return jsonify({"the answer is " : product})

# below we run the application
app.run(debug=True)