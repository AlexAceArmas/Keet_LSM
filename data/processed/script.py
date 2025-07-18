import os
FOLDER_TRAIN = "1X5U26XMihNRwZYvDxV1yOJ3jpI_QRc1Q"
FOLDER_TEST = "1G6knHfRtQXmqQ9fYGBDJ4ZyRlVfXcTML"
DEST_DIR = "data/processed_yolo_ready"

os.makedirs(f"{DEST_DIR}/train", exist_ok=True)
os.makedirs(f"{DEST_DIR}/test", exist_ok=True)

print("Downloading train folder...")
os.system(f"gdown --folder {FOLDER_TRAIN} -O {DEST_DIR}/train")

print("Downloading test folder...")
os.system(f"gdown --folder {FOLDER_TEST} -O {DEST_DIR}/test")

