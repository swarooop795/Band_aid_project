# Assignment Details:
# 1. Create a Python program that can take a photo of a person’s arm with a wound and digitally place a band-aid on the wound.
# 2. The program should detect the wound on the arm in the picture (you may use any method: OpenCV, Mediapipe, simple color/contour detection, etc.).
# 3. Once the wound on the arm is detected, overlay a band-aid image so it looks naturally placed (scaled and angled to fit the arm).
# 4. The result should show the original image and the modified image with the band-aid applied.

# Solution of this Problem is Mentioned Below:

import cv2
import numpy as np

# Load transparent PNG band-aid
def load_png(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img.shape[2] == 3:
        b, g, r = cv2.split(img)
        a = np.ones_like(b) * 255
        img = cv2.merge([b, g, r, a])
    return img

# Template-based wound detection (WORKS FOR YOUR IMAGES)
def detect_wound_template(img, template):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_temp = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Template matching
    result = cv2.matchTemplate(gray_img, gray_temp, cv2.TM_CCOEFF_NORMED)

    # Best match location
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Coordinates
    x, y = max_loc
    h, w = gray_temp.shape

    return x, y, w, h

def apply_band_aid(img, band, box):
    x, y, w, h = box

    # Resize band-aid to wound size
    band = cv2.resize(band, (w, h))

    # Split channels
    b, g, r, a = cv2.split(band)
    alpha = a / 255.0

    roi = img[y:y+h, x:x+w]

    blended = (roi * (1 - alpha[..., None]) + cv2.merge([b, g, r]) * alpha[..., None]).astype(np.uint8)
    img[y:y+h, x:x+w] = blended

    return img

def process(imgpath, bandpath, templatepath):
    img = cv2.imread(imgpath)
    band = load_png(bandpath)
    template = cv2.imread(templatepath)

    # detect wound using template
    x,y,w,h = detect_wound_template(img, template)

    result = apply_band_aid(img.copy(), band, (x,y,w,h))
    combined = np.hstack([img, result])

    cv2.imshow("Before                                                                                                 After", combined)

    save = imgpath.replace(".jpg", "_bandaid_template.jpg")
    cv2.imwrite(save, result)
    print("Saved:", save)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

process("arm1.jpg", "band_aid.png", "wound_template.png")
process("arm2.jpg", "band_aid.png", "wound_template1.png")  
process("arm3.jpg", "band_aid.png", "wound.png") 