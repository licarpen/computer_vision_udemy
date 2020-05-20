import cv2
import numpy as np

# FUNCTION
def draw_circle(event, x, y, flags, params):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x, y), 20, (255, 0, 0), 10)

# DISPLAYING THE IMAGE

img = cv2.imread('../DATA/dog_backpack.png')
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)

while True:
    cv2.imshow('my_drawing', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()