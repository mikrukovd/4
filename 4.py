from PIL import Image

image = Image.open("example.jpg")

x,y = 25,0

rgb_image = image.convert("RGB")

red, green, blue = rgb_image.split()

coordinates_red_left = (x*2, y, red.width, red.height-y)
coordinates_red_middle = (x, y, red.width-x, red.height-y)
red_left = red.crop(coordinates_red_left)
red_middle = red.crop(coordinates_red_middle)
red_corp = Image.blend(red_left,red_middle, 0.5)

coordinates_blue_right = (0, y, blue.width-x*2, blue.height-y)
coordinates_blue_middle = (x, y, blue.width-x, blue.height-y)
blue_middle = blue.crop(coordinates_blue_middle)
blue_right = blue.crop(coordinates_blue_right)
blue_corp = Image.blend(blue_middle,blue_right, 0.5)

coordinates_green_middle = (x, y, green.width-x,green.height-y)
green_middle = green.crop(coordinates_green_middle)

new_image = Image.merge("RGB",(red_corp, green_middle,blue_corp))

new_image.save("example_new.jpg")
new_image.thumbnail((80,80))
new_image.save("example_80x80.jpg")

