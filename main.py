#!/usr/bin/python3
from PIL import Image, ImageDraw
import random

# img = Image.new(mode, size, color)
# img.save(filename)

class Palette:

    def __init__(self, name, colors=[]):
        '''Palette Constructor'''
        self.name = name
        self.colors = colors

    def load_palette_from_image(self, image):
        '''loads palette from an image file'''
        return

    def load_palette_from_txt(self, filename):
        '''loads palette from a text file'''
        with open(filename, 'r') as file:
            print(f"Opening file \"{file.name}\"")
            content = file.read().splitlines()
        for color in content:
            
            self.colors.append(color)
        file.close()
        print(f"loaded palette with colors: f{self.colors}")
        return

    def random_color(self):
        '''returns a random color from the current palette'''
        return self.colors[random.randint(0, len(self.colors))]

def open_image(path):
    '''returns image from <path>'''
    return Image.open(path)

def generate_random_image(palette):
    '''randomizes the pixels in the image with colors from the palette'''
    image = Image.new("RGB", (16, 16))
    for x in range(16):
        for y in range(16):
            image[x][y] = palette.random_color()
    image.show()
    return

if __name__ == "__main__":

    test_pal = Palette("Test Palette")
    test_pal.load_palette_from_txt("test.txt")
    generate_random_image(test_pal)
