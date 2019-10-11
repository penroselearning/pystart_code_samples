
try:

    from PIL import Image, ImageEnhance

    # Reads the Image
    im = Image.open('YourImageFile.jpg')
    # Replace the File Name with an appropriate image file on your computer

    # Displays the Existing image
    im.show()

    # Use the Contrast Feature on the Image
    enh = ImageEnhance.Contrast(im)
    # Applies a Contrast value of +2.5 and displays the Image
    enh.enhance(2.5).show("Increase Contrast")

except ModuleNotFoundError:
    print('Kindly import the PIL Library')