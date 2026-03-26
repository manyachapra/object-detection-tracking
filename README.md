# Object Detection and Tracking from Video

## Description
This project performs real-time object detection and tracking from video using YOLOv8 and DeepSORT.
The system detects objects in each frame and assigns unique IDs to track them across the video.

## Technologies Used
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- DeepSORT
- NumPy

## Project Structure

object-detection-tracking
│
├── main.py
├── requirements.txt
├── README.md
├── videos/input.mp4
└── output/

## Installation

Install required libraries:

pip install -r requirements.txt

or

pip install opencv-python
pip install ultralytics
pip install deep-sort-realtime
pip install numpy

## How to Run

1. Put video inside videos folder
2. Name video as input.mp4
3. Run command:

python main.py

## Output

The program will open a window showing:
- Object detection
- Object tracking
- Unique ID for each object

## Course

Computer Vision BYOP Project

## Author

MANYA CHAPRA