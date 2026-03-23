```ruby
███╗   ███╗███████╗████████╗
████╗ ████║██╔════╝╚══██╔══╝
██╔████╔██║███████╗   ██║
██║╚██╔╝██║╚════██║   ██║
██║ ╚═╝ ██║███████║   ██║
╚═╝     ╚═╝╚══════╝   ╚═╝
```
[![Cybersecurity Projects](https://img.shields.io/badge/Cybersecurity--Projects-Project%20%239-red?style=flat&logo=github)][![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org)[![PyPI](https://img.shields.io/pypi/v/metadata-scrubber?color=3775A9&logo=pypi&logoColor=white)](https://pypi.org/project/metadata-scrubber/)
Privacy-focused CLI tool that strips sensitive metadata from images and PDFs.

> This is a quick overview — full architecture and advanced features coming soon.

---

## ⚡ What It Does

- Strip metadata from JPEG, PNG, and PDF files  
- Removes GPS coordinates, author info, timestamps, and device details  
- Simple and fast CLI-based tool  
- Batch processing support for folders  
- Preview metadata before removal  
- Clean file output without altering content  

---

## 🚀 Quick Start

```bash
pip install pillow PyPDF2
python main.py -f input.jpg -s

## 💡 Tip
Use the -s flag to show metadata before removing it.

python main.py -f input.jpg -s

| Command       | Description                               |
| ------------- | ----------------------------------------- |
| `-f <file>`   | Clean metadata from a single file         |
| `-d <folder>` | Clean metadata from all files in a folder |
| `-s`          | Show metadata before cleaning             |

## OUTPUT
python main.py -f test_files/input.jpg

Input File → Detect Type → Extract Data → Remove Metadata → Save Clean File

metadata_scrubber/
│── main.py
│── test_files/
│── README.md
