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
            self.colors.append((float(color_arr[3]), (int(color_arr[0]), int(color_arr[1]), int(color_arr[2]))))
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

    def __init__(self, name, colors=[]):
        '''Palette Constructor'''
        self.name = name
        self.colors = colors
        self.color_prob = {}

    def load_palette_from_txt(self, filename):
        print("Cannot Load a LWPalette from a text file yet")

    def load_palette_from_image(self, filename):
        '''Loads a LW Palette from an image'''
        image = Image.open(filename)

        color_list = image.getcolors()
        print(f"List of Colors in Picture: {color_list}")

        for num, color in color_list:
            self.colors.append(color)

        # print(self.colors) #DEBUG


        for color in self.colors:
            self.color_prob.update({color : {}})
            for c in self.colors:
                self.color_prob[color].update({c : 0})


        w, l = image.size
        for x in range(w):
            for y in range(l):
                curr_color = image.getpixel((x, y))
                # print(f"current color: {curr_color}") #DEBUG
                if x > 0: #make sure there is a pixel to the left
                    left_color = image.getpixel((x-1, y))
                    self.color_prob[curr_color][left_color] += 1
                elif x < w-1: #make sure there is a pixel to the right
                    right_color = image.getpixel((x+1, y))
                    self.color_prob[curr_color][right_color] += 1
                if y > 0: #make sure there is a pixel above
                    up_color = image.getpixel((x, y-1))
                    self.color_prob[curr_color][up_color] += 1
                elif y < l-1: #make sure the is a pixel below
                    down_color = image.getpixel((x, y+1))
                    self.color_prob[curr_color][down_color] += 1

        print(self.color_prob) #DEBUG
        return

    def random_color(self, curr_color):
        # print(self.color_prob[curr_color])
        total_prob = 0
        for color, prob in self.color_prob[curr_color].items(): #calculating maximum roll
            total_prob += prob

        roll = random.random() * total_prob
        for color, prob in self.color_prob[curr_color].items():
            roll -= prob
            if roll <= 0:
                return color

        return self.colors[0]

def open_image(path):
    '''returns image from <path>'''
    return Image.open(path)

def generate_random_image(palette, size=(16,16)):
    '''randomizes the pixels in the image with colors from the palette'''
    image = Image.new("RGBA", size)
    i, j = size
    prev_color = palette.colors[0]
    for x in range(i):
        for y in range(j):
            prev_color = palette.random_color(prev_color)
            image.putpixel((x, y), prev_color)
    image.show()
    return

def generate_markov_image(size, palette):
    '''markov chain image generator using only colors from the palette'''
    return

if __name__ == "__main__":

    test_pal = LWPalette("Test Palette")
    test_pal.load_palette_from_image("TestImages/bomb.png")
    generate_random_image(test_pal, (16, 16))
