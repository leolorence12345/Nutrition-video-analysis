import cv2
import os

video_path = "smart_tracked_WhatsApp Video 2025-09-10 at 05.16.56_9874c762.mp4"
thumbnail_path = "video_thumbnail.jpg"

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video {video_path}")
    exit(1)

# Get total frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"Total frames: {total_frames}")

# Extract frame from middle of video
frame_number = total_frames // 2
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

ret, frame = cap.read()
if ret:
    # Convert BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Save as JPEG
    cv2.imwrite(thumbnail_path, frame)
    print(f"✅ Thumbnail saved to {thumbnail_path}")
else:
    print("Error: Could not read frame")

cap.release()

