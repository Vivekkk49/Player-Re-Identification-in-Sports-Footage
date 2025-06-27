# Soccer Player Re-Identification - Report

## Task
Track players in a 15-second soccer video feed and keep consistent IDs even when players leave and re-enter the frame.

## Approach
- Used YOLOv11 to detect players in each frame.
- Used Deep SORT to track players with consistent IDs.
- Used OpenCV to display tracking results.
- Saved output to a video file.

## Tools Used
- YOLOv11 (for player detection)
- Deep SORT (for tracking and ID matching)
- OpenCV (for drawing rectangles and saving output)

## Challenges
- IDs sometimes switched when players overlapped.
- Limited video duration meant quick tracking decisions.

## Improvements (Future Work)
- Add jersey number recognition for stronger ID matching.
- Use more stable tracking with Kalman Filters or ByteTrack.

## Output
Final tracking video saved as: