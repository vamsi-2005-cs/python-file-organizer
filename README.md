# python-file-organizer
This Python script automatically organizes files in a given folder by sorting them into categorized directories such as Images, Videos, Documents, Music, Archives, and Others based on file extensions.

## Features
- Organizes files automatically into folders
- Supports Images, Videos, Documents, Music, Archives
- Moves unknown file types into `Others`
- Easy to use with a single input path
- Works on any folder (Downloads, Desktop, etc.)

## Requirements
- Python 3.x

## How It Works
- The script scans all files in the selected folder
- It checks file extensions
- Matches each file with predefined categories
- Moves files into respective folders automatically

## Installation

```bash
git clone https://github.com/vamsi-2005-cs/python-file-organizer.git
```
```bash
cd python-file-organizer
```

## Usage
1. Run the script: python fileOrganizer.py
2. Enter the folder path when prompted:
Enter folder path to organize: C:\Users\Vamsi\Downloads
3. The script will automatically organize files.

## Code Explanation
- `os.listdir()` → Reads all files in the folder  
- `os.path.splitext()` → Extracts file extension  
- `shutil.move()` → Moves files to new folders  
- `os.makedirs()` → Creates category folders if not present  
- File types are grouped in a dictionary for easy classification

## Sample Output

```text
photo.jpg -> Images
movie.mp4 -> Videos
notes.pdf -> Documents
song.mp3 -> Music
archive.zip -> Archives
random.xyz -> Others
Done!
```

## Author
vamsi-2005-cs
