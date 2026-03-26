import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLO model
model = YOLO("yolov8s.pt")

# Initialize tracker
tracker = DeepSort(max_age=30)

cap = cv2.VideoCapture("videos/input.mp4")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Output video
out = cv2.VideoWriter(
    "output/result.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    20,
    (width, height),
)

class_names = model.names

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Object detection
    results = model(frame, conf=0.5)[0]

    detections = []

    for r in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = r
        detections.append(([x1, y1, x2-x1, y2-y1], score, int(class_id)))

    # Tracking
    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, w, h = track.to_ltrb()

        l, t, w, h = int(l), int(t), int(w), int(h)

        label = f"ID {track_id}"

        cv2.rectangle(frame, (l, t), (w, h), (0,255,0), 2)

        cv2.putText(
            frame,
            label,
            (l, t-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,255,0),
            2
        )

    # Save output video
    out.write(frame)

    cv2.imshow("Detection & Tracking", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()