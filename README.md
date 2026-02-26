# python-threat-simulation

## Description

In this repository, I develop foundational threat simulation code for my cybersecurity course.

The purpose of this project is strictly educational: to understand how certain types of malicious software operate internally so that they can be analyzed, detected, and mitigated.

---

## Project Structure

```
python-threat-simulation/
│
├── README.md
│
├── keylogger/
│   └── keylogger.py
│
└── ransomware/
    ├── ransomware.py
    └── decrypt.py
```

## Keylogger Simulation

The "keylogger" directory contains a Python script that demonstrates how keystroke logging works at a technical level.

### Educational Objectives

- Understand how keyboard input can be intercepted
- Observe how modifier keys (CTRL, ALT, SHIFT, CMD) are handled
- Learn how special keys are processed
- Study how logs are written and modified dynamically

### Technical Overview

The implementation uses:

- pynput for capturing keyboard events
- Event listeners for key press and key release
- Modifier state tracking
- Logging output to a local file (log.txt)
- Basic handling of backspace by modifying the log file content

### Security Concepts Covered

- User input monitoring
- Behavioral detection challenges
- Privacy implications
- File manipulation techniques

This module exists to help students understand how such threats function in real-world scenarios and how defensive mechanisms can detect them.

---

## Ransomware Simulation

The "ransomware" directory contains a simplified educational example of file encryption and decryption using symmetric cryptography.

It is not designed for real-world malicious deployment, but to demonstrate the mechanics behind ransomware-style encryption.

### encrypt.py

Responsible for:

- Generating a cryptographic key
- Saving the key locally
- Searching for files within a target directory
- Encrypting file contents using symmetric encryption (Fernet)

Concepts explored:

- Symmetric encryption
- File system traversal
- Binary file handling
- Key persistence

---

### decrypt.py

Responsible for:

- Loading the previously generated key
- Locating encrypted files
- Restoring original file contents

Concepts explored:

- Key management
- Reversible cryptographic operations
- Data restoration process

---

## Requirements

- Python 3.8+
- pip

Install dependencies:

pip install pynput cryptography

---

## Recommended Testing Environment

To prevent accidental damage:

- Use a virtual machine (VirtualBox, VMware, etc.)
- Disable network access when testing
- Work only inside dedicated test directories
- Create VM snapshots before execution

---

## Academic Purpose

This repository is intended to:

- Support cybersecurity education
- Demonstrate how certain classes of malware operate
- Encourage defensive thinking and threat analysis
- Provide controlled examples for classroom discussion

Understanding offensive techniques is essential for building effective defensive strategies.

---