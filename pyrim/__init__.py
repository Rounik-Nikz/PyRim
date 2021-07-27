from PIL import Image, ImageFilter


def rotateImage(picture : str, degree : int):
    image = Image.open(picture).rotate(degree)
    option = input("Do to you want to save the rotated image : ").lower()
    if 'yes' in option:
        imageName = input("Enter the name of the file your image should be saved (with file format) : ")
        image.save(f"rotated_{imageName}")
    else:
        image.show(picture)


def blurImage(picture : str, intensity : int):
    image = Image.open(picture).filter(ImageFilter.GaussianBlur(intensity))
    option = input("Do to you want to save the blurred image : ").lower()
    if 'yes' in option:
        imageName = input("Enter the name of the file your image should be saved (with file format) : ")
        image.save(f"blurred_{imageName}")
    else:
        image.show(picture)


def contourImage(picture : str):
    image = Image.open(picture).filter(ImageFilter.CONTOUR)
    option = input("Do to you want to save the contoured image : ").lower()
    if 'yes' in option:
        imageName = input("Enter the name of the file your image should be saved (with file format) : ")
        image.save(f"contoured_{imageName}")
    else:
        image.show(picture)


def edgeEnhanceImage(picture : str):
    image = Image.open(picture).filter(ImageFilter.EDGE_ENHANCE_MORE)
    option = input("Do to you want to save the edgeEnhanced image : ").lower()
    if 'yes' in option:
        imageName = input("Enter the name of the file your image should be saved (with file format) : ")
        image.save(f"edgeEnhanced_{imageName}")
    else:
        image.show(picture)


def embossImage(picture : str):
    image = Image.open(picture).filter(ImageFilter.EMBOSS)
    option = input("Do to you want to save the embossed image : ").lower()
    if 'yes' in option:
        imageName = input("Enter the name of the file your image should be saved (with file format) : ")
        image.save(f"embossed_{imageName}")
    else:
        image.show(picture)


def findEdgesImage(picture : str):
    image = Image.open(picture).filter(ImageFilter.FIND_EDGES)
    option = input("Do to you want to save the findEdges image : ").lower()
    if 'yes' in option:
        imageName = input("Enter the name of the file your image should be saved (with file format) : ")
        image.save(f"edges_{imageName}")
    else:
        image.show(picture)