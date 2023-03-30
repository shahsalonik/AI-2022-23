from math import log
import random

filename = "star_data.csv"
star_info_dict = {}

with open(filename, "r") as f:
    count = 0
    for line in f:
        if count != 0:
            line = line.strip().split(",")
            temp = (log(float(line[0])), log(float(line[1])), log(float(line[2])), float(line[3]))
            star_type = line[4]
            star_info_dict[temp] = star_type
        else:
            count += 1

def k_means(k_value, k_elems):
    k_mean_dict = {}
    
    for i in k_elems:
        k_mean_dict[i] = []

    for star in star_info_dict.keys():
        closest_k = k_value_closest(star, k_elems)
        k_mean_dict[closest_k].append(star)
    
    return k_mean_dict

def recalculate_k_means(k_dict, k_elems):
    new_k_elems = []
    for key, s in k_dict.items():
        new_temp, new_lum, new_rad, abs_mag = 0, 0, 0, 0
        for t in s:
            new_temp += t[0]
            new_lum += t[1]
            new_rad += t[2]
            abs_mag += t[3]
        new_temp = float(new_temp / len(s))
        new_lum = float(new_lum / len(s))
        new_rad = float(new_rad / len(s))
        abs_mag = float(abs_mag / len(s))
        new_k_elems.append((new_temp, new_lum, new_rad, abs_mag))

    is_not_stable = False

    for x in new_k_elems:
        if x not in k_elems:
            is_not_stable = True
    
    return is_not_stable, new_k_elems

def k_value_closest(star_values, k_element_list):
    min_distance = distance_formula(star_values, k_element_list[0])
    result_k = k_element_list[0]
    for k in k_element_list:
        if min_distance == None:
            min_distance = distance_formula(star_values, k)
            result_k = k
        elif (x := distance_formula(star_values, k)) < min_distance:
            min_distance = x
            result_k = k
    return result_k

def distance_formula(star_tuple, k_mean_value):
    distance = 0
    for x in range(len(star_tuple)):
        distance += ((star_tuple[x] - k_mean_value[x]) ** 2)
    return (distance ** 0.5)

def print_type(k_dict_final):
    for key, val in k_dict_final.items():
        print(str(key) + ":")
        for s in val:
            print(str(s) + ": Type " + star_info_dict[s])
        print()

k_elements = random.sample(star_info_dict.keys(), 6)
is_not_stable = True

while is_not_stable:
    new_k_mean_dict = k_means(6, k_elements)
    is_not_stable, new_k_elements = recalculate_k_means(new_k_mean_dict, k_elements)
    k_elements = new_k_elements

print_type(new_k_mean_dict)
