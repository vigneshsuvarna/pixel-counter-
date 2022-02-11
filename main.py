import cv2
import numpy as np
img = cv2.imread('test.jpg')

print(img.shape)  # Print image shape
cv2.imshow("original", img)
#rs = cv2.resize(img,500,500)
#cv2.imshow("rs",rs)
# Cropping an image
cropped_image = img[180:280, 10:330]
# Display cropped image
cv2.imshow("cropped", cropped_image)
# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)
#rs = cv2.resize(cropped_image,50,50)
#cv2.imshow("rs",rs)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# importing libraries
#import cv2
#import numpy as np

# reading the image data from desired directory
#img = cv2.imread("test.jpg")
Im = cv2.cvtColor(cropped_image,cv2.COLOR_RGB2GRAY)
cv2.imshow('Image', Im)

# counting the number of pixels
print(Im.shape)
#print(Im)
count = 0
for i in Im:
    print(i)
    for j in i:
        if j >= 100 or j<=101:
            count = count +1
print(count)

number_of_white_pix = np.sum(Im == 255)
#number_of_black_pix = np.sum(Im[4:60])
#for a in range ( 1 ,254 )
number_of_grey_pix = np.sum(Im > 0 )
number_of_2_pix = np.sum(Im == 2 )
number_of_2_pix = np.sum(Im == 2 )


total_gray_pixel = (number_of_grey_pix + number_of_2_pix)
print('Number of white pixels:', number_of_white_pix)
#print('Number of black pixels:', number_of_black_pix)
print('Number of gray pixels:', number_of_grey_pix)
print('Number of gray pixels:', number_of_2_pix)
print('Number of total :',total_gray_pixel )
print('Total pixel count in range :',count)
if total_gray_pixel in range(5000,80000):
    print ("okay")

else:
    print("no")

cv2.waitKey(0)