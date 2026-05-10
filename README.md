# Title: Object Detection and Tracking from Video using YOLOv8 and DeepSORT

---

## 1. Abstract

Object detection and tracking is an important task in computer vision which is used in surveillance, autonomous driving, robotics, and video analysis.

This project implements real-time object detection and tracking from video using YOLOv8 and DeepSORT algorithms.

The system detects objects in each frame of a video and assigns unique IDs to track them across frames.

The model used is a pretrained YOLOv8 model trained on the COCO dataset.

The project demonstrates how deep learning and computer vision techniques can be used for real-time video processing.

---

## 2. Introduction

Computer vision is a field of artificial intelligence that enables computers to understand images and videos.

Object detection identifies objects in an image, while object tracking follows the detected objects across frames in a video.

### Applications of Object Detection and Tracking

- Video surveillance
- Traffic monitoring
- Autonomous vehicles
- Security systems
- Human activity analysis

In this project, YOLOv8 is used for object detection and DeepSORT is used for object tracking.

---

## 3. Objective

The main objectives of this project are:

- To detect objects in video using YOLOv8
- To track objects across frames using DeepSORT
- To assign unique ID to each object
- To display bounding boxes around objects
- To save output video with detection results
- To implement the project using Python and OpenCV

---

## 4. Dataset Used

This project uses the pretrained YOLOv8 model which is trained on the COCO (Common Objects in Context) dataset.

### COCO Dataset Includes Objects Such As:

- Person
- Dog
- Cat
- Car
- Bottle
- Chair
- Cup
- Cow
- Bird
- Bicycle

Since the model is already trained, no additional dataset training was required for this project.

---

## 5. Tools and Technologies Used

The following tools and libraries were used:

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- DeepSORT Tracker
- NumPy
- SciPy
- FilterPy
- VS Code

---

## 6. Methodology

The project works in the following steps:

1. Read video using OpenCV
2. Pass each frame to YOLOv8 model
3. Detect objects with bounding boxes
4. Send detections to DeepSORT tracker
5. Assign unique ID to each object
6. Draw bounding box and ID on frame
7. Show output on screen
8. Save output video in output folder

The model processes each frame and tracks objects continuously.

---

## 7. Implementation

The implementation is done using Python.

### Main Steps in Code

- Load YOLOv8 model
- Initialize DeepSORT tracker
- Read input video
- Detect objects
- Track objects
- Display ID and bounding box
- Save output video

### Command to Run the Project

```bash
python main.py
```

### Input Video Path

```bash
videos/input.mp4
```

### Output Video Path

```bash
output/result.mp4
```

---

## Output Screenshot

![Output](screenshots/output.png)

---

## 8. Results

The system successfully detects and tracks objects in video.

### Features Achieved

- Real-time object detection
- Object tracking with unique ID
- Bounding box display
- Output video saved
- Multiple objects tracked

The system works correctly for different objects such as person, dog, bottle, car, etc.

### Factors Affecting Accuracy

- Video quality
- Lighting
- Model size
- Confidence threshold

---

## 9. Advantages

- Works in real time
- Uses deep learning model
- Tracks multiple objects
- Easy to run
- Uses pretrained dataset

---

## 10. Limitations

- Slow on CPU
- Sometimes wrong prediction
- Accuracy depends on video quality
- Large model reduces speed

---

## 11. Applications

- CCTV monitoring
- Traffic analysis
- Face / person tracking
- Security systems
- Sports analysis
- Robotics
- Autonomous vehicles

---

## 12. Conclusion

In this project, object detection and tracking from video was successfully implemented using YOLOv8 and DeepSORT.

The system detects objects and tracks them with unique IDs.

The project demonstrates the use of computer vision techniques for real-time video analysis.

The pretrained COCO dataset was used for detection.

The results show that the system works effectively for different objects.

