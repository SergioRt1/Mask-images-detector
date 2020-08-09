import os


def csv_generator(prefix):
    file = open('classification.csv', 'w+')
    image_names = os.listdir('results/')
    for image_name in image_names:
        if image_name.startswith(prefix):
            file.write('{},{}\n'.format(image_name, 0))
        else:
            file.write('{},{}\n'.format(image_name, 1))

    file.close()


csv_generator("faces")
