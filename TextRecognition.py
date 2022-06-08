import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class TextRecognition:
    img = cv2.imread('Images/ScannedVC.jpeg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, c = img.shape
    img = cv2.resize(img, (w//2, h//2))

    # Detecting Characters

    boxes = pytesseract.image_to_data(img)

    file = open("recognized.txt", "w+")     # opening text file
    file.write("")                          # rewriting file
    file.close()                            # file closed

    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            # print(b)
            if len(b) == 12:
                file = open("recognized.txt", "a")          # open text in append mode
                file.write(b[11])                           # extracting text to file
                file.write(" ")
                file.close()                                # File Closed
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
                cv2.putText(img, b[11], (x, y), cv2.FONT_ITALIC, 0.35, (50, 50, 255), 1)

    cv2.imshow('Result', img)
    cv2.waitKey(0)

    print('Recognized')
