# 📦 File Transfer System Using Python Sockets

This project demonstrates a simple file transfer system using **Python socket programming**. The client sends a file to the server over a TCP connection, with a graphical interface for easy file selection.

---

## 📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Code Explanation](#code-explanation)
  - [Client (`client.py`)](#client-clientpy)
  - [Server (`server.py`)](#server-serverpy)
- [Example File](#example-file)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## 🚀 Overview

This project consists of two Python scripts:

- **`client.py`** — Sends a specified file to the server using a simple Tkinter GUI.
- **`server.py`** — Listens for incoming connections and receives files sent from the client.

The file transfer occurs over a **TCP socket** on **port 8090**, ensuring reliable data transmission.

---

## ✨ Features

- ✅ Send files from client to server over TCP.
- ✅ Simple GUI for selecting the file and entering the destination address.
- ✅ Progress messages indicating sending and receiving packets.
- ✅ Cross-platform support (works on Windows, macOS, Linux).

---

## ⚙️ Requirements

- **Python 3.x** 
- **Tkinter** (comes pre-installed with Python)
- Stable network connection between client and server (LAN/Wi-Fi)

---

## 🔍 Code Explanation

### 💻 Client (`client.py`)

The **client script** performs the following tasks:

1. **Creates a TCP socket** and connects to the server.
2. **Opens the file** in binary read mode (`rb`).
3. **Sends**:
   - The file name (encoded).
   - The number of packets (calculated based on file size).
   - The file data in **1024-byte chunks**.
4. Displays a **confirmation message** after successful transmission.

The GUI is built with **Tkinter**, allowing users to:
- Input the server address.
- Choose the file to send.

---

### 🖥️ Server (`server.py`)

The **server script** performs the following tasks:

1. **Creates a TCP socket** and listens for incoming connections on **port 8090**.
2. **Accepts a connection** from the client.
3. **Receives**:
   - The file name.
   - The number of packets.
   - The file data in **1024-byte chunks**.
4. Writes the received data to a new file in binary write mode (`wb`).
5. Displays **status messages** during reception to track progress.

---

## 🖼️ Example File

The project includes an example image file:

- **`flowerblue.jpg`** 🌸

You can replace this file with any other file by modifying the filename in the client GUI.

---

## ⚠️ Troubleshooting

### 🚫 Connection Issues
- Ensure both client and server are on the **same network**.
- Check if the **firewall** is blocking the connection.
- Make sure the **server is running** before starting the client.

### 📂 File Not Received
- Verify the **correct file path** is provided in the client.
- Ensure the server has **permissions** to write files in its directory.
- Try increasing the delay (`time.sleep(1)`) in `client.py` if the file is large.

### 🔑 Port Conflict
- If **port 8090** is in use, change it to an available port in both `client.py` and `server.py`:
  ```python
  port = 8090  # Change to a different port if needed

