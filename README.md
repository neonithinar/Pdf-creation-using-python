# Pdf-creation-using-python


REQUIRED PACKAGES

cv2 (OPEN CV)
matplotlib.pyplot as plt
numpy as np
pdf2image
img2pdf


PLEASE NOTE THAT THIS IS JUST A CRUDE ATTEMPT FROM A FIRST TIME LEARNER
THE CODE IS NOT CLEAN, IT HAS BUGS AT MANY PLACES ( REGARDING THE NAMING OF OUTPUT FILES )
BUT I NEEDED SOMETHING THAT GETS THE THING DONE FOR ME ASAP
CODE HAS BUGS. NEEDS YOU TO PERFORM MANY ACTIONS MANUALLY AFTER RUNNING A FFUNCTION
MOST OF IT IS NOT GENERALISED
Also THE FILENAME ISSUE. I HAVE EMPLOYED THE SOLUTION FOR THAT IN ONE OF THE FUNCTIONS 
BUT FORGOT TO USE THAT FROM THE NEXT FUNCTION ONWARDS
NOW THAT I HAVE LOST THE USE FOR THIS SCRIPT, MY LAZY ASS WON'T TAKE ANY MORE TROUBLE TO CLEAN THIS 
FILE UP AND MAKE SOMETHING ACTUALLY USEFUL FROM THIS

WHO KNOWS...! SOME DAY I MIGHT... ;)

Different functions  include:

pdf_to_image: Load a pdf or batch of pdf file from a directory and convert it into .jpeg files
              MAKE SURE THAT YOU ARE NOT LOADING A LARGE PDF WITH MANY PAGES WHEN YOU DO THIS. IT CAN USE UP THE RAM QUITE QUICKLY
              FOR MY SPECIFIC APPLICATION I HAD TO GO WITH A CUSTOM DPI OF 400. YOU CAN EITHER SET IT TO DEFAULT (200 Dpi) OR A LOWER
              VALUE

slice_images: Converts the .jpeg files in the directory to a set of sliced images. a single image is sliced into 5 parts
     which excludes the margin. returns only the rectangle containing text. 
     
join_images: takes in the sliced images from the specified directory and joins them two at a time. Overlays the stacked images on a blank canvas 
    with proper margins. Returns a batch stacked image with proper margins
    
create_pdf: joins the images from the directory specified according to order of filenames and returns a pdf file
     with the merged images
     
HOW TO EXECUTE THIS SCRIPT:
The functions required are placed in the appropriate order at the end of the script. So if you want to black box the code, 
just ==> uncomment the first function, run the code. ( check and see the filenames of the output images/ files in your root directory, I had to mannually change
            the filenames of many output image, obvitously I am too lazy to fix the minor bugs!) 
     ==> paste the output files in to the directory path of the next function
     ==> Repeat !!! 
     ==> CHECK THE HYPERPARAMETERS OF THE cv2 functions used in the functions if you need more customisation, or if you need to adjust a bunch to your specific need
          I've added quite a bunch of print statements some still active and others for debugging. check those out as well.
          
 Have fun!!!
     



