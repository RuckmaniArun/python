from flask import Flask, render_template, request, jsonify
import os

app=Flask(__name__)

@app.route("/user/<name>")
def home(name):
	#return "Hello Radha"
	return render_template("home1.html", name=name)
	#return f"Hello {name}"

@app.route("/add/<num1>/<num2>")
def add(num1,num2): 
	num1=int(num1)
	num2=int(num2)
	return {"result": num1+num2}

@app.route("/search")
def search():
	name=request.args.get("name")
	age=request.args.get("age")
	return {"Name": name, "age": age}

@app.route("/api/create",methods=["POST"])
def create_user():
	data=request.json
	data["message"]="Record created"
	return jsonify(data)

if __name__== "__main__":
	app.run(debug=True)
