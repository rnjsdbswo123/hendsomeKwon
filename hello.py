import time
import random
import os

start_time = time.time()

NUM_SAMPLES = 1000

alphabet_samples = "abcdefghijklmnopqrstuvwxyz1234567890"

def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet_samples)
    return result

first_name_sample = "김이박최정강조윤장임"
middle_name_sample = "민서예지도하주윤채현지"
last_name_sample = "준윤우원호후서연아은진"

def random_name():
    result = ""
    result += random.choice(first_name_sample)
    result += random.choice(middle_name_sample)
    result += random.choice(last_name_sample)
    return result

os.mkdir("personal_info")


for i in range(NUM_SAMPLES):
    name = random_name()

    filename = "personal_info/" + str(i) + "-" + name + ".txt"

    outfile = open(filename, 'w')

    outfile.write("name : " + name + "\n")

    outfile.write("age : " + str(start_time)[-2:] + "\n")

    outfile.write("e-mail : " + random_string(8) + "@naver.com\n")

    outfile.write("division :  " + random_string(3) + "\n")

    outfile.write("telephone : 010-" + str(start_time)[-4:] + str(start_time)[-6:-2] + "\n")

    outfile.write("sex : " + random.choice(["mail","femail"]))

    outfile.close()

