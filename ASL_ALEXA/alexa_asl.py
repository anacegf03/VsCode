import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)  # '0' is the default camera; use other numbers if you have multiple cameras

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Capture a single frame
ret, frame = cap.read()

# Release the webcam
cap.release()

# Check if the frame was captured successfully
if not ret:
    print("Error: Could not capture image.")
    exit()

# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display the original and processed images
cv2.imshow('Original Frame', frame)    # Shows the captured image
cv2.imshow('Grayscale Image', gray)    # Shows the grayscale image
cv2.imshow('Binary Image', binary)     # Shows the black and white image

# Wait for a key press and close all windows
cv2.waitKey(0)  # Wait indefinitely for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows