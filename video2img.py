import cv2
from pathlib import Path
from tqdm import tqdm

# ================= Config =================
INPUT_BASE = Path(r"G:\M3SVD_Video")  # folder containing .mp4 videos
OUTPUT_BASE = Path(r"G:\M3SVD")  # folder to save extracted frames

SPLITS = ["train", "test"]
DIRS = ["infrared_Enhance", "visible_Enhance", "infrared_noise", "visible_Blur"]

IMG_SUFFIX = ".png"  # or ".jpg"
ZERO_PAD = 6  # frame index padding: 000001, 000002, ...
# =========================================


def extract_video_to_frames(video_path: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        return

    idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        idx += 1
        out_path = out_dir / f"{idx:0{ZERO_PAD}d}{IMG_SUFFIX}"
        cv2.imwrite(str(out_path), frame)

    cap.release()


def main():
    for split in SPLITS:
        for d in DIRS:
            input_root = INPUT_BASE / split / d
            output_root = OUTPUT_BASE / split / d
            if not input_root.exists():
                continue

            videos = sorted(list(input_root.glob("*.mp4")))
            print(f"\nProcessing {split}/{d} ({len(videos)} videos)")

            for vp in tqdm(videos, desc=f"{split}-{d}", dynamic_ncols=True, ascii=True):
                # Each video corresponds to one clip folder
                clip_name = vp.stem
                extract_video_to_frames(vp, output_root / clip_name)

    print("\n✅ All frames extracted.")


if __name__ == "__main__":
    main()
