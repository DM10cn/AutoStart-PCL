# PCL2 自动重启脚本 🚀

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 项目简介 📖

这是一个用于自动化启动和关闭 **Plain Craft Launcher 2 (PCL2)** 的 Python 脚本 🐍。通过设置启动次数和延迟时间，脚本可以循环启动 PCL2 并在指定时间后关闭，适用于测试、自动化任务或重复运行场景。

本项目采用 [MIT 授权](LICENSE) 📜，欢迎自由使用、修改和分享！

---

## 功能介绍 ✨

- 🔄 **自动化启动**：循环启动 `Plain Craft Launcher 2.exe` 指定次数  
- ⏲️ **自动关闭**：在每次启动后等待指定时间再关闭程序  
- 🛠️ **进程管理**：使用 `psutil` 精确查找并关闭目标进程  
- ⚙️ **可配置参数**：支持自定义程序路径、执行次数和延迟时间  
- 📋 **错误处理**：确保进程关闭时的稳定性，输出清晰日志  

---

## 环境要求 🛠️

为了运行本脚本，请确保你的环境满足以下要求：

- **操作系统**：Windows（因脚本依赖 `psutil` 和 `.exe` 文件）  
- **Python 版本**：Python 3.8 或以上  
- **依赖库**：
  - `psutil`（用于进程管理）  
  - 安装命令：
    ```bash
    pip install psutil
    ```

---

## 部署方式 📦

1. 安装依赖模块（仅在未打包时需要）：

   ```bash
   pip install psutil
   ```

2. 使用 `PyInstaller` 工具打包脚本为 `.exe` 文件：

   ```bash
   pip install pyinstaller
   ```

3. 执行以下命令打包脚本：

   ```bash
   pyinstaller -F -i NONE your_script_name.py
   ```

   各参数含义如下：

   - `-F`：打包为单一的 `.exe` 可执行文件（否则会输出多个文件到 `dist/`）
   - `-i NONE`：不设置图标（你也可以使用 `.ico` 图标文件替代 `NONE`）

4. 成品文件将位于 `dist/` 文件夹内，复制 `your_script_name.exe` 即可部署到任何 Windows 系统中运行。

---

📄 **许可证：MIT License**  
请查看项目根目录中的 [LICENSE](./LICENSE) 文件以获取详细信息。
