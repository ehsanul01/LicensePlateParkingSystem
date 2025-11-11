import cv2
import pytesseract

def detect_license_plate(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(blur, 30, 200)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    plate = None
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        ratio = w / float(h)
        if 2 < ratio < 6:  # likely a license plate
            plate = img[y:y+h, x:x+w]
            break

    if plate is not None:
        text = pytesseract.image_to_string(plate, config='--psm 8')
        return text.strip()
    return None