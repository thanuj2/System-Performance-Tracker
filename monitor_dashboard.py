import psutil
import tkinter as tk
from tkinter import ttk
import time
import threading

# --- Function to update stats ---
def update_stats():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        uptime_seconds = time.time() - psutil.boot_time()
        uptime = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

        # Update labels
        cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
        mem_label.config(text=f"Memory Usage: {mem.percent}%")
        disk_label.config(text=f"Disk Usage: {disk.percent}%")
        uptime_label.config(text=f"System Uptime: {uptime}")

        # Update progress bars
        cpu_bar['value'] = cpu_percent
        mem_bar['value'] = mem.percent
        disk_bar['value'] = disk.percent

        time.sleep(1)

# --- Create GUI window ---
root = tk.Tk()
root.title("System Monitor Dashboard")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#222222")

# --- Labels ---
tk.Label(root, text="System Monitor Dashboard", font=("Arial", 14, "bold"), bg="#222222", fg="cyan").pack(pady=10)

cpu_label = tk.Label(root, text="CPU Usage: ", font=("Arial", 12), bg="#222222", fg="white")
cpu_label.pack()
cpu_bar = ttk.Progressbar(root, length=300, mode='determinate')
cpu_bar.pack(pady=5)

mem_label = tk.Label(root, text="Memory Usage: ", font=("Arial", 12), bg="#222222", fg="white")
mem_label.pack()
mem_bar = ttk.Progressbar(root, length=300, mode='determinate')
mem_bar.pack(pady=5)

disk_label = tk.Label(root, text="Disk Usage: ", font=("Arial", 12), bg="#222222", fg="white")
disk_label.pack()
disk_bar = ttk.Progressbar(root, length=300, mode='determinate')
disk_bar.pack(pady=5)

uptime_label = tk.Label(root, text="System Uptime: ", font=("Arial", 12), bg="#222222", fg="white")
uptime_label.pack(pady=10)

# --- Start update thread ---
t = threading.Thread(target=update_stats, daemon=True)
t.start()

root.mainloop()
