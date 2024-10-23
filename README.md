# project_forensics
Final year project

## Project Description
This project implements a real time detection of suspicious activites/ objects in surveillance videos using deep learning techniques. 

## Dataset
The dataset is collected from the following source:
"https://universe.roboflow.com/suspicious-movement/suspicious-detection/dataset/7"

It has the following classes:
names: ['normal-action', 'suspicious-suspect', 'victim', 'weapon']

total images used for training: 3,622
total images available for testing: 172

## The final model is stored in:
"./mk1/runs/detect/custom_yolov8l2/weights/best.pt"

## Real Time Detection:
Run the `real_time_detection.py` file to start the real time detection using the trained model.