# About PyRim
**PyRim is a Simple and Efficient Image Manipulation Module.**

**Author**  : **[Rounik Mondal](https://rounik.herokuapp.com/)**

**Version** : **0.1**

# Installation
```python
pip install pyrim
```

### Funtions Used
```bash
rotateImage           --> Takes two positional argument (picture : str, degree : int)
blurImage             --> Takes two positional argument (picture : str, intensity : int)
contourImage          --> Takes one positional argument (picture : str)
edgeEnhanceImage      --> Takes two positional argument (picture : str)
embossImage           --> Takes two positional argument (picture : str)
findEdgesImage        --> Takes two positional argument (picture : str)
```

### Arguments Used
```bash
picture               --> str : ImageSource of the image file with format which needs to be edited
degree                --> int : Degree to which the picture should be rotated in "rotateImage" Method
intensity             --> int : Intensity of the blur which should be implemented on the image in "blurImage" Method
```


## How To Use

```python
import pyrim

pyrim.rotateImage("yourImage.format", int)     #--> example : pyrim.rotateImage("my_image.png", 90) 
pyrim.blurImage("yourImage.format", int)       #--> example : pyrim.blurImage("my_image.png", 20)
pyrim.contourImage("yourImage.format")         #--> example : pyrim.contourImage("my_image.png")
pyrim.edgeEnhanceImage("yourImage.format")     #--> example : pyrim.edgeEnhanceImage("my_image.png")
pyrim.embossImage("yourImage.format")          #--> example : pyrim.embossImage("my_image.png")
pyrim.findEdgesImage("yourImage.format")       #--> example : pyrim.findEdgesImage("my_image.png")
```


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


# License
[MIT](https://github.com/Rounik-Nikz/PyRim/blob/main/LICENSE.txt)<br />
Copyright (c) Rounik Mondal, All Rights Reserved
