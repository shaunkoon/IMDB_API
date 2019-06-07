from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/newpost", methods = ["POST"])
def newpost():
    return "Wasssup"


    #coneciton to data base
    # params = request.data
    # params_dict = json.loads(params)
    # connection.insert(paramdicr[])
    # commit

# @app.route("/create-movie")
# def