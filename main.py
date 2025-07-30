import subprocess
import time
import psutil
import os

# 设置参数
app_path = r"C:\app"  #请在此处粘贴pcl2.exe的具体目录
app_name = "Plain Craft Launcher 2.exe"  
repeat_count = 99  # 执行次数
delay_time = 4    # 打开后等待时间

def close_app_by_name(name):
    closed = False
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] and proc.info['name'].lower() == name.lower():
            try:
                proc.terminate()
                proc.wait(timeout=3)
                print(f"已关闭：{name}")
                closed = True
            except Exception as e:
                print(f"关闭失败: {e}")
    if not closed:
        print("未发现程序运行中。")

for i in range(repeat_count):
    print(f"\n第 {i+1} 次启动：{app_path}")
    subprocess.Popen(app_path)
    time.sleep(delay_time)

    print(f"尝试关闭：{app_name}")
    close_app_by_name(app_name)
