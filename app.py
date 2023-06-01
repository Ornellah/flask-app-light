from flask import Flask, render_template, request
from functions import date_time #, pred_and_show_image
import warnings
import urllib.request
# import tensorflow as tf
# import requests

warnings.filterwarnings('ignore')
date = date_time()
app = Flask(__name__)

# Page d'acceuil
@app.route('/', methods=['GET'])
def app_home():
    #1. Afficher sur le front la date et l'heure

    return render_template("index.html", date=date)


# Page d'action
@app.route('/submit/', methods=['POST', 'GET'])
def result():


    # 2. Charger le model

    # model = tf.keras.models.load_model("model.h5")
    # print("Model loaded")

    if request.method == 'POST':
        path = "./static/assets/img.jpeg"
        try:
            image_url = request.form['input_text']
            image = requests.get(image_url,allow_redirects=True)
            
            open(path, 'wb').write(image.content)
            result = pred_and_show_image(model, path)
            
            
            # 3. Récupérer l'image uploadée par l'utilisateur puis obtenir la prédiction du model
            return render_template("submit.html",
                                   
                                   # 4. Afficher la prédiction du model sur le front
                                    prediction=result[0],
                                    img = image_url,
                                    accuracy = result[1]
                                  )       
        except:
            return render_template("submit.html")

if __name__ == '__main__':
    app.run()