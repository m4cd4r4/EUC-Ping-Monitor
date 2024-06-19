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

### Email Notification

When the device becomes reachable, the application will automatically generate an email draft to notify you. This email includes the hostname and a message that the device is now reachable.

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
