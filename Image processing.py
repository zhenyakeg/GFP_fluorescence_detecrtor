import numpy as np
import cv2
import os
import argparse

parser = argparse.ArgumentParser(description='Organoids selection')

parser.add_argument('-i', '--input', required=True, type=str,
                    help="Full input path for your experiment with scanned plates inside.")
parser.add_argument('-t', '--types', required=False, type=str, default=[".png", ".tif"],
                    help="Image types you are going to analyse.")
parser.add_argument('-pt', '--pixel_threshold', required=False, type=int, default=9,
                    help="Pixel threshold applied to your images.")
parser.add_argument('-it', '--image_threshold', required=False, type=int, default=589,
                    help="Image score threshold applied to your images.")
parser.add_argument('-f', '--filter_size', required=False, type=int, default=3,
                    help="Median filter radius applied to your images for smoothing.")
parser.add_argument('-r', '--rolling_ball', required=False, type=int, default=0,
                    help="If >0 radius for rolling ball background subtraction applied to your images.")
parser.add_argument('-a', '--alpha', required=False, type=float, default=1.4,
                    help="Contrast enhansement.")
parser.add_argument('-b', '--beta', required=False, type=int, default=10,
                    help="Brightness enhansement.")

args = parser.parse_args()

# experiment = "./Organoids"
# extensions = [".png", ".tif"]
# plates = [f.path for f in os.scandir(experiment) if f.is_dir()]
# threshold_pixel = 5
# threshold_image = 600
# filter_size = 3
# rolling_ball_radius = 0

experiment = str(args.input)
extensions = [str(x) for x in args.types]
threshold_pixel = int(args.pixel_threshold)
threshold_image = int(args.image_threshold)
filter_size = int(args.filter_size)
rolling_ball_radius = int(args.rolling_ball)
alpha = float(args.alpha) # Simple contrast control
beta = int(args.beta)   
plates = [f.path for f in os.scandir(experiment) if f.is_dir()]
print("opening experinment: " + experiment)

distribution = open(experiment + '/distr.txt', 'w')

total_count = 0
def conditioned_subtraction(a, b):
    if a > b:
        return np.uint8(a - b)
    else:
        return 0


def process_image(img, threshold, radius, filter_size):
    if radius == 0:
        # print (np.max(img))
         # Simple brightness control
        img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
        a = np.average(img[:, [int(0.1 * img.shape[1]), int(0.9 * img.shape[1])]])
        b = np.average(img[[int(0.1 * img.shape[0]), int(0.9 * img.shape[0])], :])

        # print(img[:, [int(0.1 * img.shape[1]), int(0.9 * img.shape[1])]])

        background = int((a + b) / 2)

        # background_matrix = background * np.ones(img.shape)
        # img = np.array(np.vectorize(lambda x: x if x>0 else 0)(np.array(img, dtype=np.int8) - background), dtype=np.uint8)

        # img = np.array(np.vectorize(conditioned_subtraction)(img, background), dtype=np.uint8)

    img = np.vectorize(conditioned_subtraction, otypes=[np.uint8])(img, background)

    # for i in range(img.shape[0]):
    #     for j in range(img.shape[1]):
    #         if img.item(i, j) > background:
    #             img.itemset((i, j), img.item(i, j) - background)
    #         else:
    #             img.itemset((i, j), 0)

    ret, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    cv2.medianBlur(img, filter_size, img)

    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
    #                            cv2.THRESH_BINARY, 11, 2)

    # print(background)

    # cv2.subtract(img, background)

    # print(np.max(img))

    # elif (radius > 0):
    #
    #
    #     # TODO

    return img, background


for plate in plates:

    print("opening plate: " + plate)

    out = open(plate + '/log.txt', 'w')
    layout = open(plate + '/layout.txt', 'w')
    layout.write("experiment: " + experiment + '\n')
    layout.write("plate: " + plate + '\n')
    out.write("experiment: " + experiment + '\n')
    out.write("plate: " + plate + '\n')
    num = 0
    table = [[0 for i in range(12)] for i in range(8)]

    organoids = os.listdir(plate)

    # print(organoids)
    for organoid in organoids:
        for extension in extensions:
            if organoid.endswith(extension):
                print("opening organoid: " + organoid)

                img = cv2.imread(plate + "/" + organoid, 0)

                print("processing organoid: " + organoid)

                # print(img)

                img, average_background = process_image(img, threshold_pixel, rolling_ball_radius, filter_size)

                saving_directory = plate + '/' + 'changed/'
                if (not os.path.isdir(saving_directory)):
                    os.mkdir(saving_directory)

                cv2.imwrite(saving_directory + organoid, img)

                img_score = np.count_nonzero(img == 255)

                print ('Score: ' + str(img_score))

                

                

                if img_score > threshold_image:
                    total_count += 1
                    distribution.write(str(total_count) + ' ' + str(img_score) + '\n')

                if img_score > threshold_image:
                    num += 1
                    out.write("selected image # " + str(num) + " " + organoid + "\n")
                    out.write("background subtracted:" + str(average_background) + "\n")
                    out.write("treshold applied: " + str(threshold_pixel) + "\n")
                    out.write("score: " + str(img_score) + "\n")

                    name = str(organoid)
                    row = ord(name[0]) - 65
                    column = int(name[1:3]) - 1

                    table[row][column] = 1
    out.close()
    layout.write("    " + "  ".join(map(str, range(1, 11))) + " " + " ".join(map(str, range(11, 13))))
    layout.write("\n\n")
    for i in range(len(table)):
        layout.write(chr(65 + i) + "   " + "  ".join(map(str, table[i])))
        layout.write("\n")
    layout.close()
distribution.close()

