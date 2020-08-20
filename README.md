# Mask images detector

## Description
Laboratory for the NUTE course at Escuela Colombiana de Ingeniería Julio Garavito. 

### Problem 
Scientists have shown that wearing a mask could dramatically slow down the infection rate of COVID-19 so in order to help we propose an intelligent system that recognizes a person's face and decides whether or not a person is wearing a mask.


**Achievements**

* Fetch 3000+ images using an images scrapper built on top of Selenium (Google and Bing)
* Prepare images using cv2 tools
* Model training and evaluation
* Some anomalies predictions


### How to develop


#### Feed the data set

You can take a look at the scrappers scripts in the  `scrapper` folder, the one called `scrapper.py` will use selenium to search images in google images and download them in your local desktop, just set the term to search for inside the script and run it!.


```
$ python scrapper.py
```

![_](https://media.giphy.com/media/fYYjdr1Ebk3Lrn03Mf/giphy.gif)



#### Prepare and label the pictures

**MANUAL STEP:** Separate the dataset in two sets, faces with masks and faces without masks 

Once you have the pictures, run the `cropping_image.py` script, this will run a face detection model in your pictures sets and will crop them to a size of `160x160` pixels. Remeber to modify the prefix inside the script if you want to change the name of the generated pictures `mask1234.jpg` i.e.


```
$ cropping_images.py
```

Then run the `classification_csv_generator.py` script to generate a csv file with the labels of your pictures, 

```
$ classification_csv_generator_images.py
```

#### Features and models


Go to [the jupyter file](https://github.com/SergioRt1/NUTI/blob/master/face_recognition_section2.ipynb) and run the notebook, modify the `path` variable to point to the dataset, inside this repo you can find a big data set of 3500 pictures `dataset.zip`.

 The expected structure of the data set folder is: 
 ```
dataset-root:
    - *.jpg // full data set of images in forma jpg, those images with masks sould have the prefix `masks` in the name and those without masks shoudl have the prefix `faces`
    - anomalies  // folder with pictures considered anomalies to the main data set

 ```


The notebook contains a couple of feature descriptors and ML models combinations that you can feed and play with.

