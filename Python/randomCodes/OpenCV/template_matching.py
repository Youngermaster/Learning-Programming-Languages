import cv2
import numpy as np

def template_matching(source_image_path, template_image_path, threshold=0.6):
    # Read the source image and template image
    source_img = cv2.imread(source_image_path)
    template_img = cv2.imread(template_image_path)

    # Convert images to grayscale
    source_gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)

    # Get the width and height of the template
    w, h = template_gray.shape[::-1]

    # Perform template matching
    res = cv2.matchTemplate(source_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Get the locations of good matches
    loc = np.where(res >= threshold)
    
    # Draw rectangles around the matches
    for pt in zip(*loc[::-1]):  # Switch columns and rows
        cv2.rectangle(source_img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # Save the result
    cv2.imwrite('result.png', source_img)

    # Display the result
    cv2.imshow('Detected', source_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Replace 'source.png' and 'template.png' with your image paths
template_matching('source.png', 'crop.png')
