import cv2
import os

# Initialize the camera (0 is typically the built-in camera or plug and play camera)
cap = cv2.VideoCapture()

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Create a folder called "pictures" if it doesn't exist
if not os.path.exists("pictures"):
    os.makedirs("pictures")

# Initialize a variable to count captured pictures
picture_count = 0

# Loop to continuously capture and display frames from the camera
while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the captured frame in a window
    cv2.imshow('Camera Feed', )

    # Check for key presses
    key = cv2.waitKey(1)

    # Press 'q' to exit the camera application
    if key & 0xFF == ord('q'):
        break

    # Press 'c' to capture and save a picture
    if key & 0xFF == ord('c'):
        picture_count += 1
        picture_filename = os.path.join("pictures", f"picture_{picture_count}.jpg")
        cv2.imwrite(picture_filename, frame)
        print(f"Picture saved as {picture_filename}")

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

