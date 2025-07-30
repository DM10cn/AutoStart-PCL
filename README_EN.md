[简体中文](./README.md)

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

## 🚀 Deployment Instructions

This project is a pure Python script. It can be run directly or packaged into a standalone executable (`.exe`) for Windows, allowing deployment without requiring a Python environment.

### 🧩 Steps:

1. Install dependencies (only required if not packaging):

   ```bash
   pip install psutil
   ```

2. Use `PyInstaller` to package the script into a `.exe` file:

   ```bash
   pip install pyinstaller
   ```

3. Run the following command to generate the executable:

   ```bash
   pyinstaller -F -i NONE your_script_name.py
   ```

   Explanation of parameters:

   - `-F`: Package into a single `.exe` file (otherwise outputs multiple files to the `dist/` folder)
   - `-i NONE`: No icon specified (you may replace `NONE` with a `.ico` file path to add a custom icon)

4. The final executable will be located in the `dist/` directory. Copy `your_script_name.exe` to any Windows machine to run it directly.

---

📄 **License: MIT License**  
Please see the [LICENSE](./LICENSE) file in the root of the repository for more details.
