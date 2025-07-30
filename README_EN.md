# PCL2 Auto-Restart Script 🚀

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Project Overview 📖

This is a Python script 🐍 designed to automate the launch and shutdown of **Plain Craft Launcher 2 (PCL2)**.  
By configuring the number of times and delay between runs, the script can repeatedly start and stop PCL2 — ideal for testing, automation tasks, or repetitive execution scenarios.

This project is licensed under the [MIT License](LICENSE) 📜. Feel free to use, modify, and share it!

---

## Features ✨

- 🔄 **Automated Launching**: Repeatedly starts `Plain Craft Launcher 2.exe` for a set number of times  
- ⏲️ **Auto Termination**: Waits a specific delay before closing the application after each launch  
- 🛠️ **Process Management**: Utilizes `psutil` to precisely detect and terminate the target process  
- ⚙️ **Configurable Parameters**: Easily customize program path, repeat count, and delay time  
- 📋 **Error Handling**: Ensures graceful shutdown and prints clear logs during execution  

---

## Requirements 🛠️

To run this script, make sure your environment meets the following conditions:

- **Operating System**: Windows (due to reliance on `psutil` and `.exe` handling)  
- **Python Version**: Python 3.8 or higher  
- **Dependencies**:
  - `psutil` (for process control)  
  - Install with:
    ```bash
    pip install psutil
    ```

---
## 🚀 Deployment

This project is a pure Python script that can be run directly or packaged as a standalone executable (`.exe`) for Windows, allowing deployment without a Python environment.

### 🧩 Steps:

1. Install the required module (only needed if not packaging):

   ## 🚀 Deployment

This project is a pure Python script that can be run directly or packaged as a standalone executable (`.exe`) for Windows, allowing deployment without a Python environment.

### 🧩 Steps:

1. Install the required module (only needed if not packaging):

 ```bash
 pip install psutil
 ```

2.	Use PyInstaller to convert the script into an .exe file:

```bash
pip install pyinstaller
```

3.	Run the following command to package the script:

```bash
pyinstaller -F -i NONE your_script_name.py
```

Explanation of the arguments:
	•	-F: Packages the script into a single .exe executable (otherwise, multiple files will be output to dist/)
	•	-i NONE: No icon is set (you can replace NONE with a .ico icon file if desired)

4.	The final executable will appear in the dist/ folder. Copy your_script_name.exe to any Windows system to run.

📄 License: MIT License
See the LICENSE file in the root directory for details.
