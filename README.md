ODN Python Assignment - README

📁 Folder Structure:
--------------------
ODN_Python_Assignment/
│
├── input/                    - Put all your original images here
├── output/                   - This will store cropped images (Task 2 output)
├── task1_border_detection.py - Detects borders and generates border_report.csv
├── task2_border_removal.py   - Removes detected borders and saves cropped images
├── border_report.csv         - Auto-generated report from Task 1

✅ Requirements:
----------------
Make sure you have the following Python packages installed:
- opencv-python
- numpy
- pandas

You can install them using:
> pip install opencv-python numpy pandas

▶️ How to Run:
--------------
1. TASK 1: Border Size Detection
--------------------------------
> python task1_border_detection.py

This will:
- Read all images from "input/" folder
- Detect border size (top, bottom, left, right)
- Save a CSV report to "border_report.csv"

2. TASK 2: Border Removal
-------------------------
> python task2_border_removal.py

This will:
- Read images from "input/" folder
- Automatically remove detected borders
- Save cropped versions into the "output/" folder

📌 Notes:
---------
- Ensure the "input/" folder contains sample images before running.
- "output/" will be created automatically if it doesn't exist.

Good luck with your assignment!
