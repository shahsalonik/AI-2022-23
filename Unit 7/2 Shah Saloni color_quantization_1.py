from PIL import Image
import random
import sys
from time import perf_counter

K_VALUE = int(sys.argv[2])

distance_dict = {}
color_count = {}
color_loc_dict = {}

# consider implementing a matrix (what the sub said today)
# how would that work
# smth like a tuple of tuples possibly?:

weighted_matrix = ((1, 0, 7/16), (-1, 1, 3/16), (0, 1, 5/16), (1, 1, 1/16))

img = Image.open(sys.argv[1])
#img.show() # Send the image to your OS to be displayed as a temporary file
#img2.show()
pix = img.load()

def naive_27(image, p):
    for w in range(image.size[0]):
        for l in range(image.size[1]):
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
    image.show()
    image.save("kmeansout.png")

def naive_8(image, p):
    # naive 8 color quantization
    for w in range(image.size[0]):
        for l in range(image.size[1]):
            new_list = []
            for x in p[w,l]:
                y = 0
                if x < 128:
                    y = 0
                else:
                    y = 255
                new_list.append(y)
            p[w,l] = tuple(new_list)
    image.show()
    image.save("kmeansout.png")

coord_list = []
pix_list = []

for w in range(img.size[0]):
    for l in range(img.size[1]):
        coord_list.append((w, l))
        pix_list.append(pix[w,l])
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

def k_means_plus_plus(k_value):
    k_element_list = [pix_list[random.randint(0, len(pix_list) - 1)]]

    while len(k_element_list) < k_value:
        calc_distance = [0] * len(pix_list)
        for ind, pixel in enumerate(pix_list):
            min_dist = float("inf")
            for k_elem in k_element_list:
                dist = ((pixel[0] - k_elem[0]) ** 2) + ((pixel[1] - k_elem[1]) ** 2)
                if dist < min_dist:
                    min_dist = dist
            calc_distance[ind] = min_dist

        total_distance = sum(calc_distance)
        weighted_probability_list = [y / total_distance for y in calc_distance]

        k_elem_to_add = pix_list[random.choices(range(len(pix_list)), weights = weighted_probability_list)[0]]
        k_element_list.append(k_elem_to_add)

    return k_element_list

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

#MUST RETURN SQUARED DISTANCE
def distance_formula(pixel, k_mean_value):
    distance = 0
    distance += ((pixel[0] - k_mean_value[0]) ** 2)
    distance += ((pixel[1] - k_mean_value[1]) ** 2)
    distance += ((pixel[2] - k_mean_value[2]) ** 2)
    return distance

def dithering_old(new_image, old_image):
    old_pix = old_image.load()
    new_pix = new_image.load()
    width, height = new_image.size
    for h in range(height):
        for w in range(width):
            old_pixel = new_pix[w, h]
            new_pixel = old_pix[w, h]
            new_pix[w, h] = new_pixel
            quant_error = tuple([old_pixel[i] - new_pixel[i] for i in range(3)])
            if w + 1 < width:
                new_pix[w + 1, h] = tuple([int(new_pix[w + 1, h][i] + quant_error[i] * 0.4375) for i in range(3)])
            if (w + 1 < width) and (h + 1 < height):
                new_pix[w + 1, h + 1] = tuple([int(new_pix[w + 1, h + 1][i] + quant_error[i] * 0.0625) for i in range(3)])
            if h + 1 < height:
                new_pix[w, h + 1] = tuple([int(new_pix[w, h + 1][i] + quant_error[i] * 0.3125) for i in range(3)])
            if (h + 1 < height) and (w - 1 >= 0): 
                new_pix[w - 1, h + 1] = tuple([int(new_pix[w - 1, h + 1][i] + quant_error[i] * 0.1875) for i in range(3)])
    return new_image

def dithering_new(color_list, image):
    width, height = image.size
    local_pix = image.load()

    for h in range(height):
        for w in range(width):
            old_pixel = local_pix[w, h]

            # find the pixel with the smallest error
            ind = 0
            min_error = float('inf')
            for i, num in enumerate(color_list):
                dist = distance_formula(old_pixel, num)
                if dist < min_error:
                    ind = i
                    min_error = dist
            new_pixel = color_list[ind]

            quant_error = tuple([old_pixel[x] - new_pixel[x] for x in range(3)])

            for add_w, add_h, weight in weighted_matrix:
                added_w = add_w + w
                added_h = add_h + h

                if abs(added_w) < width and abs(added_h) < height:
                    new_pixel = list(local_pix[added_w, added_h][i] + quant_error[i] * weight for i in range(3))
                    new_pixel = tuple((round(new_pixel[0]), round(new_pixel[1]), round(new_pixel[2])))
                    local_pix[added_w, added_h] = new_pixel

    return image

start = perf_counter()

frequency_list = []

for pix_val, freq in color_count.items():
    frequency_list.append((freq, pix_val))

frequency_list.sort(reverse = True)

k_elements = [frequency_list[i][1] for i in range(K_VALUE)]
is_not_stable = True

while is_not_stable:
    new_k_mean_dict = k_means(k_elements)
    is_not_stable, new_k_elements = recalculate_k_means(new_k_mean_dict, k_elements)
    k_elements = new_k_elements

#round final rgb values
for fin_col in k_elements:
    new_fin0 = round(fin_col[0])
    new_fin1 = round(fin_col[1])
    new_fin2 = round(fin_col[2])
    k_fin_round = (new_fin0, new_fin1, new_fin2)
    for c in new_k_mean_dict[fin_col]:
        for c_loc in color_loc_dict[c]:
            pix[c_loc[0], c_loc[1]] = k_fin_round

# adding color palette at the bottom of the image
color_palette = list(set(pix_list))

img = dithering_new(color_palette, img)

box = img.size[0] // K_VALUE

color_images = Image.new("RGB", (img.size[0], img.size[1] + box))

new_img = color_images.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        new_img[x, y] = pix[x, y]
    
for i in range(K_VALUE):
    for w in range(box):
        for l in range(box):
            new_img[w + (i * box), l + img.size[1]] = color_palette[i]


color_images.show()
color_images.save("kmeansout.png")

end = perf_counter()

print("Total time taken: " + str(end - start))


#k_means_plus_plus(K_VALUE) - my implementation is really slow, so I tried something else

# ORIGINAL - random.sample(color_count.keys(), K_VALUE)
    # FOR A K_VALUE OF 8
    # 1 - 34.92219294211827 seconds
    # 2 - 63.89755193796009 seconds
    # 3 - 25.54147535492666 seconds
    # 4 - 59.9034635219723 seconds
    # 5 - 30.345773437060416 seconds
    # AVERAGE - 42.922 seconds
# This is clearly very inconsistent since the keys are being chosen at random. Sometimes it's really fast, other times it's very slow.

# NEW - [frequency_list[i][1] for i in range(K_VALUE)]
    # FOR A K_VALUE OF 8
    # 1 - 33.58253590599634
    # 2 - 34.13189347810112
    # 3 - 34.66111612692475
    # 4 - 37.69707487919368
    # 5 - 34.6903032050468
    # AVERAGE - 34.952 seconds
# Extremely consistent - chooses the same values each time when it runs. This is because it chooses the most frequently ocurring RGB values in the picture.
