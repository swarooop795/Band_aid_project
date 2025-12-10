# Band_aid_project

In this project, I created a Python program that can detect a wound on a person’s arm and automatically place a digital band-aid over it. The entire process is built using OpenCV for image processing and NumPy for handling numerical operations. The workflow mainly involves detecting where the wound is, adjusting the band aid image to the right size, blending it naturally with the skin, and then showing both the original and modified images.

To locate the wound, I used template matching, which works like a “find this pattern in the larger image” technique. I first prepare a small cropped image of the wound and use OpenCV’s cv2.matchTemplate() to scan the larger arm image for the closest match. This method works well because the wound templates and original images have similar color and shape characteristics.

After the wound is found, I load a transparent PNG band-aid so its alpha channel is preserved. I resize the band-aid to the size of the detected wound, extract the transparency layer, and apply alpha blending. This ensures the band-aid merges smoothly with the skin rather than appearing pasted or artificial. Finally, I combine the before-and-after images side by side and display them using cv2.imshow().

Overall, this project demonstrates a simple but effective way to automate wound detection and apply a realistic digital band-aid using classical image processing techniques without needing complex or heavy deep-learning models.
