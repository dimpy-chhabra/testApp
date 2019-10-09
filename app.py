
from flask import Flask, render_template, request

	
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
	#name = request.get_data()
	#num = split(str(name)) 
	return "Hello!!"
   	

if __name__ == "__main__":
	app.run()	