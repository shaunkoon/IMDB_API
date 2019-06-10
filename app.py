from connect import *
from flask import Flask, request, json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/message", methods = ["POST"])
def message():
    return "Wasssup"


@app.route("/create-movie", methods = ["POST"])
def create_movie():
    params = request.data
    params_dict = json.loads(params)
    connection = Conct_MS_SQL_IMDB([[params_dict["titleType"], params_dict["primaryTitle"], params_dict["originalTitle"],
                      params_dict["startYear"], params_dict["runtimeMinutes"], params_dict["genres"]]])

    connection.insert()
    # connection.insert(params_dict["titleType"], params_dict["primaryTitle"], params_dict["originalTitle"],
    #                   params_dict["startYear"], params_dict["runtimeMinutes"], params_dict["genres"])

    connection.dockr_conct.commit()
    return "yay"

if __name__ == "__main__":
    app.run(debug=True,port=1010)
