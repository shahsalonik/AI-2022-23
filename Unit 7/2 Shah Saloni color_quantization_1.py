from PIL import Image
import random

K_VALUE = 8

distance_dict = {}

img = Image.open("puppy.jpg") # Just put the local filename in quotes.
img2 = Image.open("puppy.jpg") # Just put the local filename in quotes.
#img.show() # Send the image to your OS to be displayed as a temporary file
#img2.show()
print(img.size) # A tuple. Note: width first THEN height. PIL goes [x, y] with y counting from the top of the frame.
pix = img.load() # Pix is a pixel manipulation object; we can assign pixel values and img will change as we do so.
#pix2 = img2.load()


'''
# naive 27 color quantization
for w in range(img.size[0]):
    for l in range(img.size[1]):
        new_list = []
        for x in pix[w,l]:
            y = 0
            if x < (255 // 3):
                y = 0
            elif x > (255 * 2 // 3):
                y = 255
            else:
                y = 127
            new_list.append(y)
        pix[w,l] = tuple(new_list)

# naive 8 color quantization
for w in range(img2.size[0]):
    for l in range(img2.size[1]):
        new_list = []
        for x in pix2[w,l]:
            y = 0
            if x < 128:
                y = 0
            else:
                y = 255
            new_list.append(y)
        pix2[w,l] = tuple(new_list)
'''
coord_list = []

for w in range(img.size[0]):
    for l in range(img.size[1]):
        coord_list.append((w, l))

#print(pix[2,5]) # Access the color at a specific location; note [x, y] NOT [row, column].
#pix[2,5] = (255, 255, 255) # Set the pixel to white. Note this is called on “pix”, but it modifies “img”.
#img.show() # Now, you should see a single white pixel near the upper left corner
#img.save("naive_27_color.png") # Save the resulting image. Alter your filename as necessary.

#img2.show()
#img2.save("naive_8_color.png")

def k_means(k_elems):
    k_mean_dict = {}
    
    for i in k_elems:
        k_mean_dict[i] = []

    for loc in coord_list:
        closest_k = k_value_closest(pix[loc], k_elems)
        k_mean_dict[closest_k].append(loc)
    
    return k_mean_dict

def k_value_closest(pixel, k_element_list):
    min_distance = distance_formula(pixel, k_element_list[0])
    result_k = k_element_list[0]
    for k in k_element_list:
        if (x := distance_formula(pixel, k)) < min_distance:
            min_distance = x
            result_k = k
    return result_k

def recalculate_k_means(k_dict, k_elems):
    new_k_elems = []
    for key, s in k_dict.items():
        new_red, new_green, new_blue = 0, 0, 0
        print(k_dict)
        print(len(s))
        input()
        for t in s:
            new_red += pix[t][0]
            new_green += pix[t][1]
            new_blue += pix[t][2]
        new_red = float(new_red / len(s))
        new_green = float(new_green / len(s))
        new_blue = float(new_blue / len(s))
        new_k_elems.append((new_red, new_green, new_blue))

    is_not_stable = False

    for x in new_k_elems:
        if x not in k_elems:
            is_not_stable = True
    
    return is_not_stable, new_k_elems

def distance_formula(pixel, k_mean_value):
    if pixel in distance_dict.keys():
        return distance_dict[pixel]
    distance = 0
    distance += ((pixel[0] - k_mean_value[0]) ** 2)
    distance += ((pixel[1] - k_mean_value[1]) ** 2)
    distance += ((pixel[2] - k_mean_value[2]) ** 2)
    distance_dict[pixel] = distance
    return distance

def pick_random_pixels(image, k_vals):
    random_list = set()
    pix_set = set()
    pix = image.load()
    while len(random_list) < k_vals:
        w = random.randint(0, image.size[0])
        l = random.randint(0, image.size[1])
        if pix[w,l] not in pix_set:
            random_list.add((w, l))
            pix_set.add(pix[w,l])
    return list(pix_set)

k_elements = pick_random_pixels(img, K_VALUE)
is_not_stable = True

while is_not_stable:
    new_k_mean_dict = k_means(k_elements)
    is_not_stable, new_k_elements = recalculate_k_means(new_k_mean_dict, k_elements)
    k_elements = new_k_elements

for colors, pixs in new_k_mean_dict.items():
    for p in pixs:
        pix[p][0] = colors[0]
        pix[p][1] = colors[1]
        pix[p][2] = colors[2]

img.show()
img.save("k_means_8")
