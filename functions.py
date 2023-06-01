import time
# from cv2 import imread, resize


def date_time():
    day = time.localtime().tm_mday
    month = time.localtime().tm_mon
    year = time.localtime().tm_year
    return f'{day}/{month}/{year}'

 
def pred_and_show_image(model, img_url='static/assets/img.jpg'):

    img = resize(imread(img_url), (500, 500)).reshape(1, 500, 500, 3)/255
    pred = model.predict(img)[0][0]
    
    dict_value = {'0': 'Chien', '1': 'Chat'}
    class_predict = dict_value[str(int(pred> 0.5))]
    
    print(f"Prediction : {class_predict}")
    print(f"Probabilité : {pred}")
    return class_predict, pred