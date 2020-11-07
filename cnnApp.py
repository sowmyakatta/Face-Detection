from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
from predict import MyPredictor
from my_utils.utils import decodeImage

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self, filename):
        self.filename = filename
        self.classifier =MyPredictor(self.filename)

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    image = request.form["mytext"]
    image = image.split("base64,")[1]
    decodeImage(image, clApp.filename)
    result =clApp.classifier.myPredict()
    print(result)
    return render_template("Predicted result.html", result=result)

if __name__=="__main__":
    clApp = ClientApp("test2.jpg")
    app.run(port=8000, debug=True)
