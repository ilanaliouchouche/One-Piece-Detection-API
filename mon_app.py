from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)

model = tf.keras.models.load_model('static/op_modelV2.h5')

class_dict = {
    1: 'Ace',
    2: 'Akainu',
    3: 'Brook',
    4: 'Chopper',
    5: 'Crocodile',
    6: 'Franky',
    7: 'Jinbei',
    8: 'Kurohige',
    9: 'Law',
    10: 'Luffy',
    11: 'Mihawk',
    12: 'Nami',
    13: 'Rayleigh',
    14: 'Robin',
    15: 'Sanji',
    16: 'Shanks',
    17: 'Usopp',
    18: 'Zoro'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modele', methods=['POST'])
def modele():
    if 'image' in request.files:
        image = request.files['image']
        print(image)  # Vérifier si l'image est correctement récupérée
        img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_COLOR)
        print(img)  # Vérifier si l'image est correctement décodée
        img_resize = tf.image.resize(img, (224, 224))
        print(img_resize)  # Vérifier la forme de l'image redimensionnée
        prediction = model.predict(np.expand_dims(img_resize, 0))
        print(prediction)  # Vérifier les résultats de la prédiction
        res = np.argmax(prediction)
        character = class_dict.get(res + 1)
        return character
    else:
        return 'Erreur: Aucune image trouvée'

if __name__ == '__main__':
    app.run()