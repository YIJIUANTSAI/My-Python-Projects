

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red_avg, green_avg, blue_avg):
    r_diff = pixel.red - red_avg
    g_diff = pixel.green - green_avg
    b_diff = pixel.blue - blue_avg
    color_dist = (r_diff ** 2 + g_diff ** 2 + b_diff ** 2) ** 0.5
    return color_dist


def get_average(pixels):
    red_total = 0
    green_total = 0
    blue_total = 0
    for pixel in pixels:
        red_total += pixel.red
        green_total += pixel.green
        blue_total += pixel.blue
    count = len(pixels)
    red_avg = red_total // count
    green_avg = green_total // count
    blue_avg = blue_total // count
    return [red_avg, green_avg, blue_avg]


def get_best_pixel(pixels):
    rgb_avg = get_average(pixels)  # [red_avg, green_avg, blue_avg]
    best_pixel = pixels[0]
    min_dist = get_pixel_dist(best_pixel, rgb_avg[0], rgb_avg[1], rgb_avg[2])
    for pixel in pixels:
        dist = get_pixel_dist(pixel, rgb_avg[0], rgb_avg[1], rgb_avg[2])
        if dist < min_dist:
            min_dist = dist
            best_pixel = pixel
    return best_pixel


def solve(images):
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    for y in range(height):
        for x in range(width):
            pixels = []
            for image in images:
                pixel = image.get_pixel(x, y)
                pixels.append(pixel)

            best_pixel = get_best_pixel(pixels)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
