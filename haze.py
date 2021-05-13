from PIL import Image
import glob

def slow_horizontal_variance(im):
    '''Return average variance of horizontal lines of a grayscale image'''
    width, height = im.size
    if not width or not height: return 0
    vars = []
    pix = im.load()
    for y in range(height):
        row = [pix[x,y] for x in range(width)]
        mean = sum(row)/width
        variance = sum([(x-mean)**2 for x in row])/width
        vars.append(variance)
    return sum(vars)/height

def haze(file):
    im = Image.open(file).convert('L')
    var = slow_horizontal_variance(im)
    return var
    









