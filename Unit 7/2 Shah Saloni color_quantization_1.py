from PIL import Image
import random

K_VALUE = 27

distance_dict = {}
color_count = {}
color_loc_dict = {}

img = Image.open("panda.jpg")
img2 = Image.open("panda.jpg") # Just put the local filename in quotes.
img3 = Image.open("panda.jpg") # Just put the local filename in quotes.
#img.show() # Send the image to your OS to be displayed as a temporary file
#img2.show()
print(img2.size) # A tuple. Note: width first THEN height. PIL goes [x, y] with y counting from the top of the frame.
pix = img.load()
pix2 = img2.load() # Pix is a pixel manipulation object; we can assign pixel values and img will change as we do so.
pix3 = img3.load()

def naive_27(img, p):
    for w in range(img.size[0]):
        for l in range(img.size[1]):
            new_list = []
            for x in p[w,l]:
                y = 0
                if x < (255 // 3):
                    y = 0
                elif x > (255 * 2 // 3):
                    y = 255
                else:
                    y = 127
                new_list.append(y)
            p[w,l] = tuple(new_list)
    img.show()
    img.save("naive_27_color.png")

def naive_8(img, p):
    # naive 8 color quantization
    for w in range(img2.size[0]):
        for l in range(img2.size[1]):
            new_list = []
            for x in p[w,l]:
                y = 0
                if x < 128:
                    y = 0
                else:
                    y = 255
                new_list.append(y)
            p[w,l] = tuple(new_list)
    img.show()
    img.save("naive_8_color.png")

coord_list = []

for w in range(img.size[0]):
    for l in range(img.size[1]):
        coord_list.append((w, l))
        if pix[w,l] in color_loc_dict:
            color_loc_dict[pix[w,l]].append((w,l))
        else:
            color_loc_dict[pix[w,l]] = [(w,l)]
        if pix[w,l] in color_count:
            color_count[pix[w,l]] = color_count[pix[w,l]] + 1
        else:
            color_count[pix[w,l]] = 1

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

    for c in color_count.keys():
        closest_k = k_value_closest(c, k_elems)
        k_mean_dict[closest_k].append(c)
    
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
        to_div = 0
        for t in s:
            new_red += t[0]
            new_green += t[1]
            new_blue += t[2]
            to_div += 1
        new_red = new_red / to_div
        new_green = new_green / to_div
        new_blue = new_blue / to_div
        new_k_elems.append((new_red, new_green, new_blue))

    is_not_stable = False

    for x in new_k_elems:
        if x not in k_elems:
            is_not_stable = True
    
    return is_not_stable, new_k_elems

def distance_formula(pixel, k_mean_value):
    distance = 0
    distance += ((pixel[0] - k_mean_value[0]) ** 2)
    distance += ((pixel[1] - k_mean_value[1]) ** 2)
    distance += ((pixel[2] - k_mean_value[2]) ** 2)
    return distance

k_elements = random.sample(color_count.keys(), K_VALUE)
is_not_stable = True

while is_not_stable:
    new_k_mean_dict = k_means(k_elements)
    is_not_stable, new_k_elements = recalculate_k_means(new_k_mean_dict, k_elements)
    k_elements = new_k_elements

for fin_col in k_elements:
    k_fin_round = (round(fin_col[0]), round(fin_col[1]), round(fin_col[2]))
    for color in new_k_mean_dict[fin_col]:
        for loc in color_loc_dict[color]:
            pix[loc[0], loc[1]] = k_fin_round

img.show()
img.save("k_means_27_panda.png")
