from PIL import Image


def dump_image_details(image):
    pass


def get_pillow_mode_string(in_string):
    lookup_dict = { 
        '1': '1-bit pixels, black and white, stored with one pixel per byte',
        'L' :'8-bit pixels, black and white',
        'P' :'8-bit pixels, mapped to any other mode using a color palette',
        'RGB' :'3x8-bit pixels, true color',
        'RGBA' :'4x8-bit pixels, true color with transparency mask',
        'CMYK' :'4x8-bit pixels, color separation',
        'YCbCr' :'3x8-bit pixels, color video format',
    }

    return lookup_dict.get(in_string)
# LAB (3x8-bit pixels, the L*a*b color space)
# HSV (3x8-bit pixels, Hue, Saturation, Value color space)
# I (32-bit signed integer pixels)
# F (32-bit floating point pixels)

# LA (L with alpha)
# PA (P with alpha)
# RGBX (true color with padding)
# RGBa (true color with premultiplied alpha)
# La (L with premultiplied alpha)
# I;16 (16-bit unsigned integer pixels)
# I;16L (16-bit little endian unsigned integer pixels)
# I;16B (16-bit big endian unsigned integer pixels)
# I;16N (16-bit native endian unsigned integer pixels)
# BGR;15 (15-bit reversed true colour)
# BGR;16 (16-bit reversed true colour)
# BGR;24 (24-bit reversed true colour)
# BGR;32 (32-bit reversed true colour)


def double_image_block(filename):
    """Zoom and image with block increase."""
    input_image = Image.open(filename)

    output_image = Image.new('L', input_image.size*2)


def double_image_nn():
    """Zoom an image by two using simple nearest neighbour."""
    input_image = Image.open('./images/NeptuneGrayScale.tif')

    input_size_x = input_image.size[0]
    input_size_y = input_image.size[1]
    
    print('Input image size x = {} y = {}'.format(input_size_x, input_size_y))
    output_image = Image.new('L', input_image.size * 2)
    print(output_image)
    for x in range(input_size_x):
        for y in range(input_size_y):
            v = input_image.getpixel((x, y))
            print('({},{}) = {}'.format(x, y, v))


def load_image():
    """Test the loading of an image."""
    input_image = Image.open('./images/NeptuneGrayScale.tif')
    print(input_image.format, input_image.size, input_image.mode)
    print(get_pillow_mode_string(input_image.mode))
    print(input_image.size[0], input_image.size[1])
    for x in range(input_image.size[0]):
        print("{}:{}".format(x, input_image.getpixel((x, 200))))
    print(input_image.getpixel((200, 200)))
    input_image.show()


def test_image_create():
    """Create a simple red test image."""
    img = Image.new('RGB', (60, 30), color='red')
    img.save('pil_red.png')


def main():
    load_image()
    #double_image_block('./images/NeptuneGrayScale.tif')
    #double_image_nn()


if __name__ == '__main__':
    main()
