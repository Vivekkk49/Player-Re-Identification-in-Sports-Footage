import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

model = YOLO('models/yolov11.pt')
tracker = DeepSort(max_age=30)

cap = cv2.VideoCapture('videos/15sec_input_720p.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0 or fps is None:
    fps = 25

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("=== Video Properties ===")
print("FPS:", fps)
print("Resolution:", width, "x", height)
print("=================================")

resize_output = True
target_width = 640
target_height = 384
output_size = (target_width, target_height) if resize_output else (width, height)

out = cv2.VideoWriter('outputs/reid_output.avi',
                      cv2.VideoWriter_fourcc(*'XVID'),
                      fps,
                      output_size)

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Reached end of video.")
        break

    # Resize the current frame
    resized_frame = cv2.resize(frame, output_size) if resize_output else frame

    # Detect players
    results = model(resized_frame)[0]
    detections = []

    for det in results.boxes.data.tolist():
        x1, y1, x2, y2, conf, cls = det
        if int(cls) == 0:
            bbox = [int(x1), int(y1), int(x2 - x1), int(y2 - y1)]
            detections.append((bbox, conf, 'player'))

    # Update tracker
    tracks = tracker.update_tracks(detections, frame=resized_frame)

    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, r, b = track.to_ltrb()
        cv2.rectangle(resized_frame, (int(l), int(t)), (int(r), int(b)), (0, 0, 255), 2)
        cv2.putText(resized_frame, f"Player {track_id}", (int(l), int(t) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    out.write(resized_frame)
    frame_count += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"✅ Done! {frame_count} frames saved to outputs/reid_output.avi")