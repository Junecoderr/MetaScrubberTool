import os
import argparse
from PIL import Image
from PIL.ExifTags import TAGS
from PyPDF2 import PdfReader, PdfWriter

# =========================
# IMAGE METADATA FUNCTIONS
# =========================

def show_image_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if exif_data:
            print("\n[+] Image Metadata Found:\n")
            for tag, value in exif_data.items():
                print(f"{TAGS.get(tag, tag)}: {value}")
        else:
            print("[-] No metadata found in image")

    except Exception as e:
        print(f"[!] Error reading image metadata: {e}")


def remove_image_metadata(input_path, output_path):
    try:
        image = Image.open(input_path)

        # Keep only pixel data
        data = list(image.getdata())
        clean_image = Image.new(image.mode, image.size)
        clean_image.putdata(data)

        clean_image.save(output_path)
        print(f"[+] Clean image saved as: {output_path}")

    except Exception as e:
        print(f"[!] Error cleaning image: {e}")


# =========================
# PDF METADATA FUNCTIONS
# =========================

def show_pdf_metadata(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        metadata = reader.metadata

        if metadata:
            print("\n[+] PDF Metadata Found:\n")
            for key, value in metadata.items():
                print(f"{key}: {value}")
        else:
            print("[-] No metadata found in PDF")

    except Exception as e:
        print(f"[!] Error reading PDF metadata: {e}")


def remove_pdf_metadata(input_pdf, output_pdf):
    try:
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        # Remove metadata
        writer.add_metadata({})

        with open(output_pdf, "wb") as f:
            writer.write(f)

        print(f"[+] Clean PDF saved as: {output_pdf}")

    except Exception as e:
        print(f"[!] Error cleaning PDF: {e}")


# =========================
# FILE HANDLER
# =========================

def process_file(file_path, show_meta=False):
    if not os.path.exists(file_path):
        print("[-] File does not exist!")
        return

    filename = os.path.basename(file_path)
    output_path = "clean_" + filename

    if file_path.lower().endswith((".jpg", ".jpeg", ".png")):
        if show_meta:
            show_image_metadata(file_path)
        remove_image_metadata(file_path, output_path)

    elif file_path.lower().endswith(".pdf"):
        if show_meta:
            show_pdf_metadata(file_path)
        remove_pdf_metadata(file_path, output_path)

    else:
        print("[-] Unsupported file type")


# =========================
# BATCH PROCESSING
# =========================

def process_folder(folder_path):
    if not os.path.exists(folder_path):
        print("[-] Folder does not exist!")
        return

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            print(f"\n[*] Processing: {file}")
            process_file(full_path)


# =========================
# MAIN CLI
# =========================

def main():
    parser = argparse.ArgumentParser(description="Metadata Scrubber Tool")

    parser.add_argument("-f", "--file", help="File to clean")
    parser.add_argument("-d", "--directory", help="Folder to clean")
    parser.add_argument("-s", "--show", action="store_true", help="Show metadata before cleaning")

    args = parser.parse_args()

    if args.file:
        process_file(args.file, args.show)

    elif args.directory:
        process_folder(args.directory)

    else:
        print("Usage:")
        print("  python main.py -f file.jpg -s")
        print("  python main.py -d folder/")


if __name__ == "__main__":
    main()