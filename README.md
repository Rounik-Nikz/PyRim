# About PyRim
**PyRim is a Simple and Efficient Image Manipulation Module.**

**Author**  : **[Rounik Mondal](https://rounik.herokuapp.com/)**

**Version** : *1.0*

# Installation
```python
pip install pyrim
```

### Classes Used
```python
Rotate
Blur
Contour
EdgeEnhance
Emboss
FindEdges
```

### Methods Used
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


# How To Use

```python
from pyrim import Rotate, Blur, Contour, Emboss, EdgeEnhance, FindEdges

#initializing classes og the module in variables

rotate = Rotate()
blur = Blur()
contour = Contour()
edge = EdgeEnhance()
emboss = Emboss()
find = FindEdges()


#excecuting codes with initialized variables

rotate.rotateImage("yourImage.format", int)   #--> example : rotate.rotateImage("my_image.png", 90) 
blur.blurImage("yourImage.format", int)       #--> example : blur.blurImage("my_image.png", 20)
contour.contourImage("yourImage.format")      #--> example : contour.contourImage("my_image.png")
edge.edgeEnhanceImage("yourImage.format")     #--> example : edge.edgeEnhanceImage("my_image.png")
emboss.embossImage("yourImage.format")        #--> example : emboss.embossImage("my_image.png")
find.findEdgesImage("yourImage.format")       #--> example : find.findEdgesImage("my_image.png")
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
MIT License

Copyright (c) 2021 Rounik Mondal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
