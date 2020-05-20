import cv2
img = cv2.imread('flipped_dog.jpg')

while True:
    cv2.imshow('window', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()