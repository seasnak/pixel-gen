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
            color_arr = color.split(' ')
            self.colors.append((int(color_arr[0]), int(color_arr[1]), int(color_arr[2])))
        file.close()
        print(f"loaded palette with colors: {self.colors}")
        return

    def random_color(self):
        '''returns a random color from the current palette'''
        return self.colors[random.randint(0, len(self.colors) - 1)]

class WPalette(Palette):
    '''Weighted Palette Class'''

    def __init__(self, name, colors=[]):
        '''Palette Constructor'''
        self.name = name
        self.colors = colors

    def load_palette_from_txt(self, filename):
        '''loads a weighted palette from a text file'''
        with open(filename, 'r') as file:
            print(f"Opening file \"{file.name}\"")
            content = file.read().splitlines()
        for color in content:
            color_arr = color.split(' ')
            self.colors.append(((int(color_arr[0]), int(color_arr[1]), int(color_arr[2])), float(color_arr[3])))
        file.close()
        print(f"loaded palette with colors: {self.colors}")
        return

    def random_color(self):
        '''returns a random color from the current palette'''
        return self.colors[random.randint(0, len(self.colors) - 1)]

def open_image(path):
    '''returns image from <path>'''
    return Image.open(path)

def generate_random_image(size, palette):
    '''randomizes the pixels in the image with colors from the palette'''
    image = Image.new("RGB", size)
    i, j = size
    for x in range(i):
        for y in range(j):
            image.putpixel((x, y), palette.random_color())
    image.show()
    return

def generate_markov_image(size, palette):
    '''markov chain image generator using only colors from the palette'''
    return

if __name__ == "__main__":

    test_pal = WPalette("Test Palette")
    test_pal.load_palette_from_txt("test.txt")
    generate_random_image((200, 200), test_pal)
