>**AUTHOR**  : Rounik Mondal
>**INFO**    : A Simple and Efficient Image Manupulation Module
>**VERSION** : 1.0

>~~-+--+--+--+--+--+-~~
>**CLASS**
>
>Rotate
>Blur
>Contour
>EdgeEnhance
>Emboss
>FindEdges
>~~-+--+--+--+--+--+-~~

>~~-+--+--+--+--+--+-~~
>**METHODS**
>
>rotateImage                 --> Takes two positional argument (picture : str, degree : int)
>blurImage                    --> Takes two positional argument (picture : str, intensity : int)
>contourImage              --> Takes one positional argument (picture : str)
>edgeEnhanceImage     --> Takes two positional argument (picture : str)
>embossImage              --> Takes two positional argument (picture : str)
>findEdgesImage           --> Takes two positional argument (picture : str)
>~~-+--+--+--+--+--+-~~

>~~-+--+--+--+--+--+-~~
>**ARGUMENTS**
>
>picture             --> str : ImageSource of the picture file format which needs to be edited
>degree             --> int : Degree to which the picture should be rotated
>intensity          --> int : Intensity of the blur which should be implemented on the image
>~~-+--+--+--+--+--+-~~



> **FOR EXAMPLE**
>
> """
> from pyrim import Rotate, Blur, Contour, Emboss, EdgeEnhance, FindEdges
>
> *#initializing module in variables*
>
> rotate = Rotate()
> blur = Blur()
> contour = Contour()
> edge = EdgeEnhance()
> emboss = Emboss()
> find = FindEdges()
>
> *#excecuting codes with initialized variables*
>
> rotate.rotateImage("yourImage.format", int)
> blur.blurImage("yourImage.format", int)
> contour.contourImage("yourImage.format")
> edge.edgeEnhanceImage("yourImage.format")
> emboss.embossImage("yourImage.format")
> find.findEdgesImage("yourImage.format")
> """
