#!/usr/bin/python3
from PIL import Image, ImageDraw

# img = Image.new(mode, size, color)
# img.save(filename)

class Palette:
    def __init__(self, name):
        self.name = name
        self.colors = []

    def __init__(self, name, colors):
        self.name = name
        self.colors = colors

    def load_palette_from_image(self, image):
        '''loads palette from an image file'''
        return

    def load_palette_from_txt(self, filename):
        '''loads palette from a text file'''
        with open(filename, 'r') as file:
            print(f"Opening file {file.name}")
            content = file.read.splitlines()
            print(content)
        file.close()
        return

    def get_random_color(self):
        '''returns a random color from the current palette'''
        return self.colors[0, random.randint(len(self.colors))]

def open_image(path):
    '''returns image from <path>'''
    return Image.open(path)

if __name__ == "__main__":
    # img = Image.new(mode, size, color)
    test_pal = Palette("Test Palette")
