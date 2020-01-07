import numpy as np
import pytesseract


import cv2

cap = cv2.VideoCapture(0)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    cv2.filter2D(gray, -1, kernel)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imwrite('e.png',gray)
    print(pytesseract.image_to_string('e.png'))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


