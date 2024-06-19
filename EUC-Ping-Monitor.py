# Macdara O Murchu
# 19.06.2024

import os
import time
import subprocess
import tkinter as tk
from tkinter import messagebox, scrolledtext, Menu, Toplevel, Text
from threading import Thread
from win10toast import ToastNotifier
import webbrowser

def check_ping(hostname, days_to_run, root, result_text):
    max_days = min(days_to_run, 30)
    check_interval = 300  # check every 5 minutes
    max_checks = (max_days * 24 * 60 * 60) // check_interval
    notifier = ToastNotifier()

    for _ in range(max_checks):
        response = subprocess.run(['ping', '-n', '1', hostname], stdout=subprocess.PIPE)
        if response.returncode == 0:
            notifier.show_toast("Ping Success", f"{hostname} is now reachable", duration=10)
            root.deiconify()
            result_text.insert(tk.END, response.stdout.decode('utf-8'))
            return
        time.sleep(check_interval)

    notifier.show_toast("Ping Timeout", f"Could not reach {hostname} within {max_days} days", duration=10)

def start_check_ping(hostname, days_to_run, root, result_text):
    try:
        days_to_run = int(days_to_run)
        if days_to_run <= 0 or days_to_run > 30:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number between 1 and 30 for Days to Run.")
        return
    
    root.withdraw()
    Thread(target=check_ping, args=(hostname, days_to_run, root, result_text)).start()

def show_about():
    about_text = """
# EUC-Ping-Monitor

## Introduction

Welcome to the Ping Monitor application! This tool helps you keep track of whether a specific computer or device on a network is reachable over the internet. It's especially useful if you need to monitor the availability of a server or any other networked device over a set period of time.

## How It Works

The Ping Monitor application operates through a simple graphical user interface (GUI) built using Python's Tkinter library. Here's a step-by-step breakdown of how it works:

### Hostname Input

You start by entering the hostname or IP address of the device you want to monitor. This is the address that the application will repeatedly check to see if it can be reached.

### Days to Run

Next, you enter the number of days you want the monitoring to run, from 1 to 30 days. This sets how long the application will continue checking the device's availability.

### Running the Check

When you click the "Run" button, the application starts a background process that tries to "ping" the device. Pinging is a way of sending a small packet of data to the device and waiting for a response, which indicates that the device is reachable. The application pings the device every 5 minutes for the duration you've set (up to 30 days).

### Notifications

- **Success**: If the device becomes reachable during the monitoring period, you will receive a notification on your computer. Additionally, the application will display the ping results in the text area of the GUI.
- **Failure**: If the device remains unreachable for the entire period, you will receive a notification indicating that the device could not be reached.

## User Interface Components

- **Hostname Entry**: A text field where you input the hostname or IP address of the device you want to monitor.
- **Days to Run Entry**: A text field where you specify the number of days (between 1 and 30) to monitor the device.
- **Run Button**: A button to start the monitoring process.
- **Result Text Area**: A scrollable text area that displays the results of each ping attempt.

## Behind the Scenes

- **Background Monitoring**: The monitoring process runs in the background, allowing you to use your computer for other tasks without interruption.
- **Notifications**: Using the `win10toast` library, the application provides toast notifications on Windows systems to alert you of the device's status.
- **Error Handling**: The application includes checks to ensure you enter valid inputs. If you enter an invalid number of days, it will prompt you to correct it.

## Getting Started

1. **Launch the Application**: Double-click the application icon to open the Ping Monitor.
2. **Enter Details**: Fill in the hostname and the number of days you want to run the check.
3. **Start Monitoring**: Click the "Run" button and let the application do the rest!
    """
    about_window = Toplevel()
    about_window.title("About EUC-Ping-Monitor")
    about_text_widget = Text(about_window, wrap='word', bg='#F0F0F0', fg='#006AFF', font=('Arial', 12))
    about_text_widget.insert(tk.END, about_text)
    about_text_widget.config(state='disabled')
    about_text_widget.pack(padx=10, pady=10, fill='both', expand=True)

def main():
    root = tk.Tk()
    root.title("Ping Monitor")
    root.configure(bg='#F0F0F0')  # Light grey background

    menu = Menu(root)
    root.config(menu=menu)

    help_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=show_about)

    tk.Label(root, text="Hostname:", bg='#F0F0F0', fg='#006AFF', font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    hostname_entry = tk.Entry(root, width=30, font=('Arial', 12))
    hostname_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Days to Run:", bg='#F0F0F0', fg='#006AFF', font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=10, pady=5, sticky='w')
    days_entry = tk.Entry(root, width=30, font=('Arial', 12))
    days_entry.grid(row=1, column=1, padx=10, pady=5)

    result_text = scrolledtext.ScrolledText(root, width=60, height=20, font=('Arial', 10))
    result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    run_button = tk.Button(root, text="Run", 
                           command=lambda: start_check_ping(hostname_entry.get(), days_entry.get(), root, result_text),
                           bg='#006AFF', fg='white', font=('Arial', 12, 'bold'))
    run_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
