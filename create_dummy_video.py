import cv2
import numpy as np
import os

def create_dummy_video(output_path, width=640, height=480, fps=10, duration_seconds=5):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Codec for .mp4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    if not out.isOpened():
        print(f"Error: Could not open video writer for {output_path}")
        return

    num_frames = fps * duration_seconds
    for i in range(num_frames):
        # Create a blank frame
        frame = np.zeros((height, width, 3), dtype=np.uint8)

        # Add some changing content to simulate scenes
        if i < num_frames / 3:
            # First scene: blue background with white circle
            frame[:, :] = (255, 0, 0) # Blue
            cv2.circle(frame, (width // 2, height // 2), 50, (255, 255, 255), -1)
        elif i < 2 * num_frames / 3:
            # Second scene: green background with red rectangle
            frame[:, :] = (0, 255, 0) # Green
            cv2.rectangle(frame, (width // 4, height // 4), (3 * width // 4, 3 * height // 4), (0, 0, 255), -1)
        else:
            # Third scene: red background with yellow text
            frame[:, :] = (0, 0, 255) # Red
            cv2.putText(frame, f"Frame {i}", (50, height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        out.write(frame)
    out.release()
    print(f"Dummy video created at: {output_path}")

if __name__ == "__main__":
    test_directory = "./test_files"
    os.makedirs(test_directory, exist_ok=True)
    output_video_path = os.path.join(test_directory, "test_video.mp4")
    create_dummy_video(output_video_path)


