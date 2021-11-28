#!/usr/bin/env python
import numpy as np
from os import system
import time

# the grid
view = np.zeros((31,31))
# 6x6 white block
b=np.ones((6,6))

# put white block on the grid
view[13:19, 3:9] = b

# dit was voor gifjes (
from PIL import Image
color_dict= {0: [0,0,0], 1: [255,255,255]}
image_array= np.ndarray(shape=(31,31,3), dtype=np.uint8)
nums = iter([str(num).zfill(4) for num in range(360)])

def draw(view, image_array):
    global nums
    imgnum = next(nums)
    for position, square in np.ndenumerate(view):
        image_array[position[1],position[0], :] = color_dict[square]
    sized_array = np.repeat(np.repeat(image_array,5, axis=0), 5, axis=1)
    image = Image.fromarray(sized_array, mode='RGB')
    image.save(f'img\\goes{imgnum}.png')
#)


# blit the view to the screen
def blit(view):
    for x in range(len(view)):
        for y in range(len(view)):
            if view[x][y] == 1:
                print("█", end="")
            else:
                print("░", end="")
        print("")

blit(view)

# oooh fancy smancy rotation matrix
# maar zonder rotation matrix
middle = np.array((15,15))
def rotate(view, angle):
    theta= np.radians(angle)
    new = view * 0
    for (x, y), value in np.ndenumerate(view):
        if not value: continue
        vector=np.array((x,y))
        # rotate vector about middle vector [15 15]      (want dat is het midden van view [31 31])
        x_new = int(np.cos((theta)) * (vector[0] - middle[0]) - np.sin((theta)) * (vector[1] - middle[1]) + middle[0])
        y_new = int(np.sin((theta)) * (vector[0] - middle[0]) + np.cos((theta)) * (vector[1] - middle[1]) + middle[0])
        new[x_new, y_new] = 1

    return(new)

input("aaaarrrrre you readdddyyyyyyyy!!!!")
while True:
    for i in range(360):
        view2=rotate(view, i)
        blit(view2)
        #draw(view2, image_array)
        time.sleep(.001)