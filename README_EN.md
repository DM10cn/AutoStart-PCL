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
