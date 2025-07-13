import os
import hashlib
import datetime
from PIL import Image, ExifTags
from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
import cv2

def get_file_metadata(file_path):
    stat_info = os.stat(file_path)
    metadata = {
        "name": os.path.basename(file_path),
        "path": file_path,
        "size": stat_info.st_size,
        "creation_time": datetime.datetime.fromtimestamp(stat_info.st_ctime).isoformat(),
        "modification_time": datetime.datetime.fromtimestamp(stat_info.st_mtime).isoformat(),
        "last_access_time": datetime.datetime.fromtimestamp(stat_info.st_atime).isoformat(),
        "extension": os.path.splitext(file_path)[1].lower()
    }

    if metadata["extension"] in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]:
        try:
            img = Image.open(file_path)
            exif_data = {}
            if hasattr(img, "_getexif") and img._getexif() is not None:
                for tag, value in img._getexif().items():
                    decoded = ExifTags.TAGS.get(tag, tag)
                    exif_data[decoded] = value
            metadata["image_metadata"] = {
                "make": exif_data.get("Make"),
                "model": exif_data.get("Model"),
                "date_taken": exif_data.get("DateTimeOriginal"),
                "resolution": f"{img.width}x{img.height}"
            }
        except Exception as e:
            print(f"Error extracting image metadata from {file_path}: {e}")
    
    if metadata["extension"] in [".mp4", ".mov", ".avi", ".mkv"]:
        try:
            video_manager = VideoManager([file_path])
            scene_manager = SceneManager()
            scene_manager.add_detector(ContentDetector())

            video_manager.set_downscale_factor() # Optional: downscale video for faster processing
            video_manager.start()

            scene_manager.detect_scenes(frame_source=video_manager)
            scene_list = scene_manager.get_scene_list()

            cap = cv2.VideoCapture(file_path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = frame_count / fps if fps > 0 else 0
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            keyframes = []
            for i, scene in enumerate(scene_list):
                # Extract a frame from the middle of each scene as a keyframe
                frame_num = int((scene[0].get_frames() + scene[1].get_frames()) / 2)
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
                ret, frame = cap.read()
                if ret:
                    keyframe_path = os.path.join(os.path.dirname(file_path), f"keyframe_{os.path.basename(file_path)}_{i}.jpg")
                    cv2.imwrite(keyframe_path, frame)
                    keyframes.append(keyframe_path)

            cap.release()

            metadata["video_metadata"] = {
                "duration": duration,
                "codec": "Unknown", # More advanced analysis needed for actual codec
                "resolution": f"{width}x{height}",
                "scenes": [f"Start: {s[0].get_seconds()}s, End: {s[1].get_seconds()}s" for s in scene_list],
                "keyframes": keyframes
            }
        except Exception as e:
            print(f"Error extracting video metadata from {file_path}: {e}")

    return metadata

def calculate_md5(file_path, chunk_size=8192):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def scan_directory(path):
    file_data = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                metadata = get_file_metadata(file_path)
                metadata["hash_md5"] = calculate_md5(file_path)
                file_data.append(metadata)
                print(f"Processed file: {file_path}")
                print(f"  Metadata: {metadata}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    return file_data

if __name__ == "__main__":
    test_directory = "./test_files"
    os.makedirs(test_directory, exist_ok=True)
    
    # Create a dummy image file for testing
    try:
        from PIL import Image, ImageDraw
        img = Image.new("RGB", (60, 30), color = "red")
        d = ImageDraw.Draw(img)
        d.text((10,10), "Hello", fill=(255,255,0))
        img.save(os.path.join(test_directory, "test_image.jpg"))
        print("Created dummy image: test_image.jpg")
    except ImportError:
        print("Pillow not fully installed or missing dependencies for image creation. Skipping dummy image creation.")

    # Create a dummy video file for testing (assuming create_dummy_video.py was run)
    dummy_video_path = os.path.join(test_directory, "test_video.mp4")
    if not os.path.exists(dummy_video_path):
        print(f"Dummy video file {dummy_video_path} not found. Please run create_dummy_video.py first.")

    with open(os.path.join(test_directory, "test1.txt"), "w") as f:
        f.write("This is a test file for hashing.")
    os.makedirs(os.path.join(test_directory, "subdir"), exist_ok=True)
    with open(os.path.join(test_directory, "subdir", "test2.txt"), "w") as f:
        f.write("This is another test file for hashing.")

    print(f"Scanning directory: {test_directory}")
    scanned_files = scan_directory(test_directory)
    print("\n--- Scan Results ---")
    for file_info in scanned_files:
        print(file_info)


