import os

import cv2


def crop_images(dataset):
    image_names = os.listdir('images/')
    i = 0
    errors = 0
    for name in image_names:
        img = cv2.imread('images/' + name, cv2.IMREAD_COLOR)
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        p = 10
        faces = face_cascade.detectMultiScale(img_RGB)
        for (x, y, w, h) in faces:
            try:
                cropped_img = img_RGB[y - p + 1:y + h + p, x - p + 1:x + w + p]
                resized_img = cv2.resize(cropped_img, (160, 160), interpolation=cv2.INTER_LINEAR)
                image_name = dataset + str(i) + '.jpg'
                cv2.imwrite('results/' + image_name, cv2.cvtColor(resized_img, cv2.COLOR_RGB2BGR))
                i += 1
                print("Done", i)
            except:
                errors += 1
                print("Error in image: {}, faces: {}, #{}".format(name, faces, errors))


crop_images("faces")
