import pyautogui
import time


def sleep():
    time.sleep(1)

while True:
# Get the current position of the mouse cursor
    # x, y = pyautogui.position()

    # print("The current position of the mouse cursor is ({}, {})".format(x, y))

    def next():
        pyautogui.click(1862,609, duration=1)
    next()

    sleep()

    def click_visible_in_webshop():
         pyautogui.click(402,908, duration=1)
    click_visible_in_webshop()

    sleep()
#  Get the current position of the mouse cursor
#     x, y = pyautogui.position()
#     print("The current position of the mouse cursor is ({}, {})".format(x, y))
# import pyautogui
# import time
# import cv2

# def sleep():
#     time.sleep(1)

# img = cv2.imread("image.png")
# img2 = cv2.imread("image2.png")
# while True:
   

#     # Perform a click at (1862, 609)
#     click = pyautogui.click(1862, 609, duration=1 )

#     sleep()

#     # Check if the image is visible on the screen
#     result = pyautogui.locateOnScreen(img)

#     # If the image is found, perform a click at (402, 908)
#     if result is not None:
#         pyautogui.click(402, 908, duration=1)
#     else:
#         pyautogui(click)

#     sleep()

# import pyautogui
# import time
# import cv2

# def sleep():
#     time.sleep(1)

# img = cv2.imread("image.png")
# img2 = cv2.imread("image2.png")

# import pyautogui
# import time
# import cv2

# # Define the sleep function
# def sleep():
#     time.sleep(1)

# # Load the images
# img = cv2.imread("image.png")
# img2 = cv2.imread("image2.png")


#     # Perform a click at (1862, 609)
# pyautogui.click(1862, 609, duration=1)

#     # Pause for 1 second
# sleep()

#     # Check if the first image is visible on the screen
# result = pyautogui.locateOnScreen(img)

#     # If the first image is found, perform a click at (402, 908)
# if result is not None:
#         pyautogui.click(402, 908, duration=1)
#     # If the first image is not found, check if the second image is visible on the screen
# else:
#         result2 = pyautogui.locateOnScreen(img2)
#         # If the second image is found, do nothing
#         if result2 is not None:
#             pass
#         # If neither image is found, perform a click at the current mouse position
#         else:
#             pyautogui.click()

#     # Pause for 1 second
# sleep()


