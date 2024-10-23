
import cv2
from ultralytics import YOLO

# Load your trained YOLOv8 model
model = YOLO("C:\\Users\\kruth\\project_forensics\\mk1\\runs\\detect\\custom_yolov8l2\\weights\\best.pt")


# Initialize the webcam or video stream
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam, or replace with video path for external camera/video

if not cap.isOpened():
    print("Error: Could not open video stream or file.")
    exit()

# Set up the video frame display loop
while cap.isOpened():
    # Capture each frame from the video stream
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Exiting.")
        break
    
    # Perform inference on the frame
    results = model.predict(frame, conf=0.5, show=True)  # You can adjust 'conf' (confidence threshold) as needed
    
    # Display the frame with the detections
    # results.show() will also display it, but you can manually show the frame using OpenCV:
    cv2.imshow("YOLOv8 Real-Time Detection", results[0].plot())  # plot() renders bounding boxes on the frame

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close display window
cap.release()
cv2.destroyAllWindows()
