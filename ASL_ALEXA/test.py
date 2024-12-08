import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)
image_counter = 0 

while True:
    ret, frame = cap.read()    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) #al parecer quita el sonido de la foto osea se ve mejor
    
    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) #vi que es mas recomendado hacerlo binario
    
    contours, _ = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        
        x, y, w, h = cv2.boundingRect(max_contour)
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        hand = gray[y:y+h, x:x+w]
        
        hand_28x28 = cv2.resize(hand, (28, 28))
        
        cv2.imshow("Hand 28x28", hand_28x28)
    
    cv2.imshow("Webcam Feed", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('p'):
        image_name = f"hand_image_{image_counter}.png"
        cv2.imwrite(image_name, hand_28x28)
        print(f"Saved {image_name}")
        image_counter += 1
    
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
