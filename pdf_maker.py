import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from pdf2image import convert_from_path
from PIL import Image
import img2pdf


# test_image = cv2.imread(os.path.join("/home/nithin/Downloads/practical_dl/Practical_DL_1_5.jpeg"))
# test_image = test_image[0:4520, :]
#
# test_crop_scaled = cv2.imread(os.path.join("cropped_image.jpg"))
#
# print(f"test_image shape:{test_image.shape}")
# #print(test_image.dtype)
# plt.imshow(test_image)
# plt.show()


# test_crop_scaled = cv2.imread(os.path.join("cropped_image.jpg"))
#
# print(f"Test_cropped_scaled image shape:{test_crop_scaled.shape}")
#print(test_image.dtype)
# plt.imshow(test_crop_scaled)
# plt.show()

"""
width_A4 = 210
height_A4 = 297
aspect_ratio = width_A4/height_A4
pt1 = (0, 800)
pt2 = (0, 2540)
width = euclidian_distance(pt1, pt2)
print(f"width = {width}")
height = width / aspect_ratio
print(height)
pt3 = (int(height), 2540)

"""



BLANK_CANVAS = np.ones((1852, 1310, 3), dtype=np.uint8)
BLANK_CANVAS = 255 * BLANK_CANVAS
# BLANK_CANVAS = cv2.rectangle(BLANK_CANVAS, (230, 120), (1100, 1730), (0, 255, 0), thickness= 2)
print(f" the shape of blank canvas:{BLANK_CANVAS.shape}")
# plt.imshow(BLANK_CANVAS)
# plt.show()
# cv2.imwrite("MARGINED IMAGE.jpg", BLANK_CANVAS)


PDF_ORIGINAL_PATH = os.path.join("/home/nithin/Downloads/Hands on ml/")
PATH = os.path.join("/home/nithin/Downloads/text_book/")
OUTPUT_PATH = os.path.join("/home/nithin/Downloads/folder/")

#
# crop_img = test_image[2600:4630, 1225:2085]
# plt.imshow(crop_img)
# plt.show()
# print("The shape of cropepd image: {}".format(crop_img.shape))
#




page_no = 0





def pdf_to_image(pdf_original_path):

    """
    pdf_flie = os.path.join("/home/nithin/Downloads/Practical_DL_1.pdf")
    pages = convert_from_path(pdf_flie,output_folder=os.path.join("/home/nithin/Downloads/practical_dl") , dpi= 400)
    count = 213
    img_file = pdf_flie.replace(".pdf", "")

    for page in pages:
        count+= 1
        jpeg_file = img_file + "_" + str(count) + ".jpeg"
        page.save(jpeg_file, "JPEG")
    """
    print("Running pdf to images function")
    Filenames = os.listdir(pdf_original_path)
    Filenames.sort()
    print(Filenames)
    count = 95


    for name in Filenames:
        pdf_file = str(pdf_original_path) + str(name)
        pages = convert_from_path(pdf_file, dpi= 400)


        for page in pages:
            count += 1
            jpeg_file =str(count) + ".jpeg"
            page.save(jpeg_file, "JPEG")






def euclidian_distance(point1, point2):
    """Calcuates the euclidian distance between the point1 and point2
    used to calculate the length of the four sides of the square"""
    distance = np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return distance

def slice_images(path, page_no = page_no):
    """Converts the .jpeg files in the directory to a set of sliced images. a single image is sliced into 5 parts
     which excludes the margin. returns only the rectangle containing text"""
    print("Running slice images function")
    Filenames = os.listdir(path)



    for dir_path, _, filenames in os.walk(path):
        print(dir_path)
        filenames.sort()
        for name in filenames:

            print(name)


            page_no += 1
            img = cv2.imread(os.path.join(str(dir_path)+ str(name)))
            img = img[0:4520, 1225:2085]
            img1 = img[0:904,:]
            cv2.imwrite(str(page_no)+".jpeg", img1)
            page_no += 1
            img2 = img[904:1808, :]
            cv2.imwrite(str(page_no)+".jpeg", img2)
            page_no += 1
            img3 = img[1808:2712, :]
            cv2.imwrite(str(page_no)+".jpeg", img3)
            page_no += 1
            img4 = img[2712:3616, :]
            cv2.imwrite(str(page_no)+".jpeg", img4)
            page_no += 1
            img5 = img[3616:4520, :]
            cv2.imwrite(str(page_no)+".jpeg", img5)


def sort_jpeg_names(directory_path):
    """ Searches the directory image files and returns a list of the numerically sorted values of image names """
    print("sorting jpeg names")
    for dir_path, _, filenames in os.walk(directory_path):
        print(dir_path)

        FILENAMES = []
        for filename in filenames:
            x = filename.strip(".jpeg")
            FILENAMES.append(x)

        FILENAMES.sort(key= int)

        Filenames = []
        for name in FILENAMES:
            x = str(name) + ".jpeg"
            Filenames.append(x)

        # print("sorted filenames of jpegs: ", Filenames)
        return Filenames


def join_images(output_path, canvas):

    """Joins the two adjacent images from the directory path and lays them over the BLANK PAGE  created at the
    appropriate margins"""
    print("Running join images function")
    page_no = 1
    Filenames = sort_jpeg_names(output_path)
    # print("sorted filenames of jpegs: ", Filenames)
    count = 0


    while(count != len(Filenames)):
        img1 = cv2.imread(os.path.join(str(output_path)+ str(Filenames[count])))
        count+= 1
        img2 = cv2.imread(os.path.join(str(output_path) + str(Filenames[count])))
        count += 1

        Blank_canvas = canvas.copy()

        stacked_image = np.vstack((img1, img2))
        stacked_image = cv2.resize(stacked_image, (870, 1610), interpolation=cv2.INTER_AREA)
        Blank_canvas[120:1730, 230:1100] = stacked_image
        if page_no < 1000:
            if page_no < 100:
                if page_no < 10:
                    name = str(00) + str(page_no) + ".jpeg"

                    cv2.imwrite(name, Blank_canvas)

                else:
                    name = str(0) + str(page_no) + ".jpeg"

                    cv2.imwrite(name, Blank_canvas)
            else:
                name = str(page_no) + ".jpeg"

                cv2.imwrite(name, Blank_canvas)








        page_no += 1


        print("count = ", count)


def create_pdf(pdf_path):
    """joins the images from the directory specified according to order of filenames and returns a pdf file
     with the merged images"""

    print("Running create pdf Function")
    filenames = os.listdir(pdf_path)
    filenames.sort()
    print(filenames)
    with open("my_Practical_DL.pdf", "wb") as f:
        f.write(img2pdf.convert([os.path.join(str(pdf_path)+str(name)) for name in filenames]))







PDF_PATH = os.path.join("/home/nithin/Downloads/pdf_folder/")
test_image = cv2.imread(os.path.join("/home/nithin/Downloads/practical_dl/130.jpeg"))
# test_image2 = cv2.imread(os.path.join("/home/nithin/Downloads/practical_dl/117.jpeg.jpeg"))
#
# test_image = cv2.resize(test_image, (870, 1610), interpolation=cv2.INTER_AREA)
# test_image2 = cv2.resize(test_image2, (870, 1610), interpolation=cv2.INTER_AREA)
# Blank_canvas = BLANK_CANVAS.copy()
# Blank_canvas2 = BLANK_CANVAS.copy()
# Blank_canvas[120:1730, 230:1100] = test_image
# Blank_canvas2[120:1730, 230:1100] = test_image2


# cv2.imshow("test_image", BLANK_CANVAS)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#cv2.imwrite("test_iamge.jpeg", BLANK_CANVAS)


#   CREATE PDF FROM LIST OF IMAGES


#pdf_to_image(PDF_ORIGINAL_PATH)

# slice_images(PATH)

# join_images(OUTPUT_PATH, BLANK_CANVAS)
#
# create_pdf(PDF_PATH)






