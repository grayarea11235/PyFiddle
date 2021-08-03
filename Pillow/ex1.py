from PIL import Image

def double_image_nn():
    input_image = Image.open('./images/NeptuneGrayScale.tif')
    
    input_size_x = input_image.size[0]
    input_size_y = input_image.size[1]

    print('Input image size x = {} y = {}'.format(input_size_x, input_size_y))
    output_image = Image.new('L', input_image.size)
    for x in range(input_size_x):
        for y in range(input_size_y):
            v = input_image.getpixel((x, y))
            print('{},{} = {}'.format(x, y, v))


def load_image():
    im = Image.open('./images/NeptuneGrayScale.tif')
    #print(im)
    print(im.format, im.size, im.mode)
    print(im.size[0], im.size[1])
    for x in range(im.size[0]):
        print("{}:{}".format(x, im.getpixel((x, 200))))
    print(im.getpixel((200, 200)))
    im.show()


def test_image_create():
    img = Image.new('RGB', (60, 30), color = 'red')
    img.save('pil_red.png')


def main():
    double_image_nn()
    #test_image_create()
    #load_image()


if __name__ == '__main__':
    main()
