# import yaml
# from pathlib import Path
# 
# # CONFIGURACIÓN
# dataset_dir = Path("data/processed/yolo_ready")
# class_names = ['HAND', 'FACE', 'BODY']
# output_path = dataset_dir / "data.yaml"
# 
# # CONTENIDO
# yaml_content = {
#     'train': str(dataset_dir / "images/train"),
#     'val': str(dataset_dir / "images/val"),
#     'nc': len(class_names),
#     'names': class_names
# }
# 
# # === WRITE FILE ===
# with open(output_path, 'w') as f:
#     yaml.dump(yaml_content, f, # default_flow_style=False)
# 
# print(f"data.yaml creado en: {output_path.resolve# ()}")






import yaml
from pathlib import Path

def create_data_yaml(path_to_classes_txt, output_yaml_path, base_dataset_path):
    classes_path = Path(path_to_classes_txt)
    if not classes_path.exists():
        print(f"⚠️ classes.txt not found at {classes_path}")
        return
    
    # Read class names
    with open(classes_path, 'r') as f:
        classes = [line.strip() for line in f if line.strip()]
    
    # Create YAML structure
    data = {
        'train': str(Path(base_dataset_path) / "images/train"),
        'val': str(Path(base_dataset_path) / "images/val"),
        'nc': len(classes),
        'names': classes
    }
    
    # Write YAML file
    with open(output_yaml_path, 'w') as f:
        yaml.dump(data, f, sort_keys=False)

    print(f"✅ data.yaml written to: {output_yaml_path.resolve()}")
    return

# === Paths for your project ===
path_to_classes_txt = "data/raw/yolo_export/classes.txt"
path_to_data_yaml = "data/processed/yolo_ready/data.yaml"
base_dataset_path = "data/processed/yolo_ready"

create_data_yaml(path_to_classes_txt, path_to_data_yaml, base_dataset_path)