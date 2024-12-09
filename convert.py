import sys
from PIL import Image

def convert_to_jpeg(file_path):
    try:
        img = Image.open(file_path)
        rgb_img = img.convert('RGB')
        output_path = file_path.rsplit('.', 1)[0] + ".jpg"
        rgb_img.save(output_path, 'JPEG', quality=95)
        print(f"Converted: {file_path} -> {output_path}")
    except Exception as e:
        print(f"Error converting {file_path}: {e}")

if __name__ == "__main__":
    for file in sys.argv[1:]:
        convert_to_jpeg(file)