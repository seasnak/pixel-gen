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

    def load_palette_from_image(self, filename):
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
        total_prob = 0
        for i in range(len(self.colors)):
            color, prob = self.colors[i]
            total_prob += prob

        roll = random.random() * total_prob
        for color, prob in self.colors:
            roll -= prob
            if roll <= 0:
                return color
        return (0, 0, 0)

class LWPalette(Palette):
    '''Locally Weighted Palette: Takes the probability of neighboring colors into account'''

    def load_palette_from_txt(self, filename):
        print("Cannot Load a LWPalette from a text file")

    def load_palette_from_image(self, filename):
        '''Loads a LW Palette from an image'''
        return

    def print_palette(self):
        return

def open_image(path):
    '''returns image from <path>'''
    return Image.open(path)

def generate_random_image(palette, size=(16,16)):
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
    generate_random_image(test_pal, (200, 200))
