import cv2
def main(): 
    # Load the image
    img = cv2.imread('demo02_ws/1.jpg')

    # Display the image in a window
    cv2.imshow('Image', img)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()