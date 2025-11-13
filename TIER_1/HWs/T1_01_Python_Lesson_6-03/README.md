# Directory Tree Visualizer (Python Homework -- Lesson 6, Task 3)

## Description

This project is a console utility that visualizes the structure of a
directory.\
It prints all subfolders and files in a tree-like view and uses colors
to distinguish directories, files, and log messages.

-   Folders → **cyan**
-   Files → **green**
-   Log messages → info (blue), warning (yellow), error (red)

Color output uses the `colorama` library.

------------------------------------------------------------------------

## Project Structure

    T1_01_Python_Lesson_6-03/
    │
    ├── picture/              # Sample folder for testing (matches homework example)
    │   ├── logo/
    │   │   ├── IBM+Logo.png
    │   │   ├── ibm.svg
    │   │   └── logo-tm.png
    │   ├── bot-icon.png
    │   └── mongodb.jpg
    │
    ├── log.py                # Colored logging helpers
    ├── main.py               # Main script: prints directory tree
    ├── requirements.txt      # Dependencies (colorama)
    └── .venv/                # Virtual environment

------------------------------------------------------------------------

## Requirements

-   Python 3.8+
-   `colorama`

Install dependencies:

    pip install colorama

Or from the file:

    pip install -r requirements.txt

------------------------------------------------------------------------

## Usage

### 1. Show directory tree

    python main.py <path-to-directory>

Example:

    python main.py picture

### 2. Show color log examples

    python main.py test

------------------------------------------------------------------------

## How It Works

### main.py

-   Reads arguments from command line\
-   Accepts:
    -   directory path\
    -   command `test`\
-   Checks if path exists and is a directory\
-   Prints tree using `parse_folder()`\
-   Uses colorama colors for better visualization

### parse_folder(path)

-   Sorts items (folders first)
-   Recursively prints tree structure
-   Uses unicode symbols:
    -   `┣` and `┗` for branches\
    -   `┃` for vertical structure

### log.py

Simple colored logging functions: - `log_info()` - `log_warning()` -
`log_error()`

------------------------------------------------------------------------

## Example Output (directory tree)

    📦 picture
    ┣ logo
    ┃ ┣ IBM+Logo.png
    ┃ ┣ ibm.svg
    ┃ ┗ logo-tm.png
    ┣ bot-icon.png
    ┗ mongodb.jpg

------------------------------------------------------------------------

## Example Output (test mode)

    --- DEMO: color log messages ---
    [INFO] This is an info message example.
    [WARNING] This is a warning example.
    [ERROR] This is an error example.

------------------------------------------------------------------------

## Created by:
**Author:** Oleksandr Skriabikov  
Created as part of the **Neoversity Python course, Lesson 6, Home Task 2**