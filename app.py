from flask import Flask , jsonify , render_template , request
from flask_cors import CORS , cross_origin
import os

app=Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename='inputImage.jpg'
        self.classifier=dogcat(self.filename)



@app.route('/',methods=['GET'])
@cross_origin()
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
@cross_origin()
def PredictRoute():
    image=request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)


if __name__=='__main__':
    clApp = ClientApp()
    app.run(debug=True)
