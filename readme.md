# 📂 File Search CLI Tool

A simple command-line tool built with Python that searches for a keyword inside files within a given directory.

This tool can:

- 🔎 Search file names
- 📄 Search inside text file contents
- 📁 Traverse subdirectories
- 🎯 Filter by file extension (optional)
- 🔢 Display total matches found

---

## 🚀 Features

- Recursive folder traversal using `os.walk()`
- Case-insensitive keyword matching
- Optional file extension filtering
- Handles unreadable files safely using exception handling
- Displays file path, line number, and matched content
- Counts total occurrences found

---

## 🛠 Tech Used

- Python 3
- `os` module
- File handling
- Exception handling

---

## ⚠ Notes

- Content search is performed only on text-readable files.
- Binary files are safely skipped.
- Tested using relative and absolute paths.


## 🧠 Author

Built as a hands-on Python CLI project to strengthen understanding of:

- File systems
- String matching
- Recursive directory traversal
- Basic CLI interaction