from PIL import Image


def load_image():
    im = Image.open('./images/NeptuneGrayScale.tif')
    #print(im)
    print(im.format, im.size, im.mode)
    print(im.size[0], im.size[1])
    for x in range(im.size[0]):
        print("{}:{}".format(x, im.getpixel((x, 200))))
    print(im.getpixel((200, 200)))
    im.show()


def main():
    load_image()


if __name__ == '__main__':
    main()
