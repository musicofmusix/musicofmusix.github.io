import os
from PIL import Image, ImageCms
import argparse

def ensure_srgb(image: Image.Image) -> Image.Image:
    icc = image.info.get("icc_profile")
    if not icc:
        return image

    try:
        src_profile = ImageCms.ImageCmsProfile(io.BytesIO(icc))
        dst_profile = ImageCms.createProfile("sRGB")

        has_alpha = ("A" in image.getbands())
        out_mode = "RGBA" if has_alpha else "RGB"

        # Convert image mode appropriately before applying profile
        if has_alpha and image.mode != "RGBA":
            image = image.convert("RGBA")
        elif (not has_alpha) and image.mode != "RGB":
            image = image.convert("RGB")

        return ImageCms.profileToProfile(image, src_profile, dst_profile, outputMode=out_mode)

    except Exception as e:
        print(f"ICC profile conversion failed, using original image: {e}")
        # Fallback that PRESERVES alpha if present
        return image.convert("RGBA") if ("A" in image.getbands()) else image.convert("RGB")

def convert_image_to_webp(input_path, output_path, quality):
    try:
        with Image.open(input_path) as im:
            im = ensure_srgb(im)
            im.save(output_path, "WEBP", quality=quality, method=6)
            print(f"Converted: {input_path} → {output_path}")
    except Exception as e:
        print(f"Failed: {input_path} ({e})")

def find_and_convert_images(root_dir, quality):
    supported_exts = ('.jpg', '.jpeg', '.png', '.tif', '.tiff')
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(supported_exts):
                input_path = os.path.join(subdir, file)
                output_file = os.path.splitext(file)[0] + ".webp"
                output_path = os.path.join(subdir, output_file)

                convert_image_to_webp(input_path, output_path, quality)

def main():
    parser = argparse.ArgumentParser(description="Batch convert JPG/PNG to WebP recursively with sRGB conversion.")
    parser.add_argument("root_dir", help="Root directory to search for images (e.g., assets/img)")
    parser.add_argument("--quality", type=int, default=80, help="WebP quality (0-100, default=80)")

    args = parser.parse_args()
    find_and_convert_images(args.root_dir, args.quality)

if __name__ == "__main__":
    import io
    main()
